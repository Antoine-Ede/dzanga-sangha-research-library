const GROUP_ID = "6701789";
const API = `https://api.zotero.org/groups/${GROUP_ID}`;
const state = { items: [], collections: new Map(), filtered: [], selected: {}, optionValues: {}, authorLabels: new Map(), ready: false, section:'library' };
const FILTERS = {
  categoryFilter: {param:'category',label:'Catégorie'},
  collectionFilter: {param:'theme',label:'Thème',multi:true},
  scopeFilter: {param:'scope',label:'Portée'},
  siteFilter: {param:'site',label:'Site',multi:true},
  taxonFilter: {param:'taxon',label:'Taxon',multi:true},
  methodFilter: {param:'method',label:'Méthode',multi:true},
  accessFilter: {param:'access',label:'Accès'},
  yearFilter: {param:'year',label:'Année'},
  authorFilter: {param:'author',label:'Auteur'},
  typeFilter: {param:'type',label:'Type'}
};
const TYPE_LABELS = {journalArticle:'Article de revue',book:'Livre',bookSection:'Chapitre de livre',thesis:'Thèse ou mémoire',report:'Rapport',conferencePaper:'Communication ou résumé de congrès',preprint:'Préprint',dataset:'Jeu de données',webpage:'Page web',document:'Document'};
const UNKNOWN = '__unspecified__';

const $ = (id) => document.getElementById(id);
const esc = (s="") => String(s).replace(/[&<>"']/g, c => ({'&':'&amp;','<':'&lt;','>':'&gt;','"':'&quot;',"'":'&#39;'}[c]));
const norm = (s="") => String(s).normalize("NFD").replace(/\p{Diacritic}/gu,"").toLowerCase();
const normalizedDoi = (s="") => String(s).trim().replace(/^https?:\/\/(dx\.)?doi\.org\//i, "").replace(/^doi:\s*/i, "").toLowerCase();
function safeUrl(value) {
  try { const url = new URL(value); return ["https:", "http:"].includes(url.protocol) ? url.href : ""; }
  catch { return ""; }
}
function doiOf(item) {
  return normalizedDoi(item.data.DOI || String(item.data.extra || "").match(/^DOI:\s*(\S+)/im)?.[1] || "");
}

async function fetchAll(endpoint) {
  const out = [];
  for (let start=0;;start+=100) {
    const sep = endpoint.includes("?") ? "&" : "?";
    const r = await fetch(`${endpoint}${sep}limit=100&start=${start}`, {
      headers: {"Zotero-API-Version":"3"}, signal: AbortSignal.timeout(30000)
    });
    if (!r.ok) throw new Error(`Zotero API ${r.status}`);
    const page = await r.json();
    if (!Array.isArray(page)) throw new Error("Réponse Zotero inattendue");
    out.push(...page);
    if (page.length < 100) break;
  }
  return out;
}

function tagsOf(item) {
  return LibraryModel.tags(item);
}
function yearOf(item) {
  const m = String(item.data.date || "").match(/\b(18|19|20)\d{2}\b/);
  return m ? m[0] : "";
}
function authorNames(item) {
  const cs = (item.data.creators || []).filter(c => ["author","editor"].includes(c.creatorType));
  return cs.map(c => c.name || [c.firstName,c.lastName].filter(Boolean).join(" ")).filter(Boolean);
}
function authorsOf(item) {
  const names = authorNames(item);
  if (names.length <= 4) return names.join(", ");
  return `${names.slice(0,3).join(", ")} et al.`;
}
function authorSurnames(item) {
  return (item.data.creators||[]).filter(c=>['author','editor'].includes(c.creatorType)).map(c=>c.name||c.lastName).filter(Boolean);
}
function sourceOf(item) {
  return item.data.publicationTitle || item.data.bookTitle || item.data.proceedingsTitle ||
         item.data.publisher || item.data.institution || item.data.university || item.data.repository || "";
}
function collectionNames(item) {
  return (item.data.collections || []).map(k => state.collections.get(k)).filter(Boolean);
}
function tagValues(tags,prefix) {
  return tags.filter(t => t.startsWith(prefix)).map(t => t.slice(prefix.length));
}
function canonicalUrl(item) {
  return safeUrl(item.links?.alternate?.href) || `https://www.zotero.org/groups/${GROUP_ID}/items/${encodeURIComponent(item.key)}`;
}
function articleUrl(item) {
  const doi=doiOf(item);
  return doi ? `https://doi.org/${encodeURIComponent(doi)}` : safeUrl(item.data.url);
}
function titleLink(item) {
  const title=esc(item.data.title || '(Sans titre)'),url=articleUrl(item);
  return url ? `<a href="${esc(url)}" target="_blank" rel="noopener">${title}</a>` : title;
}

function valuesOf(item, id) {
  let values;
  if (id === 'categoryFilter') values = [LibraryModel.category(item)];
  else if (id === 'collectionFilter') values = collectionNames(item).filter(v=>!/^00 |^99 /.test(v));
  else if (id === 'yearFilter') values = [yearOf(item)].filter(Boolean);
  else if (id === 'authorFilter') values = authorSurnames(item).map(v=>norm(v).trim());
  else if (id === 'typeFilter') values = [item.data.itemType].filter(Boolean);
  else values = tagValues(tagsOf(item), {scopeFilter:'SCOPE:',siteFilter:'SITE:',taxonFilter:'TAXON:',methodFilter:'METHOD:',accessFilter:'ACCESS:'}[id]);
  return values.length ? [...new Set(values)] : [UNKNOWN];
}
function optionLabel(id, value) {
  if (value === UNKNOWN) return 'Non renseigné';
  if (id === 'categoryFilter') return LibraryModel.labels[value]||value;
  if (id === 'collectionFilter') return value.replace(/^\d+ - /,'');
  if (id === 'scopeFilter') return {'DSPA-Core':'Données DSPA · Core','DSPA-Relevant':'Contexte et gestion · Relevant'}[value] || value;
  if (id === 'accessFilter') return {Open:'Accès ouvert',Restricted:'Accès restreint'}[value] || value;
  if (id === 'typeFilter') return TYPE_LABELS[value] || value;
  if (id === 'authorFilter') return state.authorLabels.get(value)||value;
  return value;
}
function populateFilters() {
  for(const item of state.items)for(const name of authorSurnames(item)){
    const key=norm(name).trim();
    if(!state.authorLabels.has(key))state.authorLabels.set(key,name);
  }
  for (const [id, config] of Object.entries(FILTERS)) {
    state.selected[id] = [];
    const values = [...new Set(state.items.flatMap(i=>valuesOf(i,id)))];
    values.sort((a,b)=>a===UNKNOWN?1:b===UNKNOWN?-1:id==='yearFilter'?Number(b)-Number(a):optionLabel(id,a).localeCompare(optionLabel(id,b),'fr',{numeric:true}));
    state.optionValues[id] = values;
    for (const value of values) {
      const option=document.createElement('option'); option.value=value; option.textContent=optionLabel(id,value); $(id).appendChild(option);
    }
  }
  const years=state.items.map(yearOf).filter(Boolean).map(Number);
  if(years.length){$('yearFrom').placeholder=String(Math.min(...years));$('yearTo').placeholder=String(Math.max(...years));}
}
function currentCriteria() {
  for (const [id,config] of Object.entries(FILTERS)) {
    const value=$(id).value;
    if(config.multi){if(value&&!state.selected[id].includes(value))state.selected[id].push(value);$(id).value='';}
    else state.selected[id]=value?[value]:[];
  }
  const from=$('yearFrom').value, to=$('yearTo').value;
  const invalid = (from && (!/^\d{4}$/.test(from)||Number(from)<1800||Number(from)>2100)) ||
    (to && (!/^\d{4}$/.test(to)||Number(to)<1800||Number(to)>2100)) || (from&&to&&Number(from)>Number(to));
  return {words:norm($('search').value.trim()).split(/\s+/).filter(Boolean),from,to,invalid,selected:state.selected};
}
function matches(item, criteria, ignore='') {
  if(criteria.invalid)return false;
  const year=yearOf(item);
  if(criteria.from&&(!year||Number(year)<Number(criteria.from)))return false;
  if(criteria.to&&(!year||Number(year)>Number(criteria.to)))return false;
  const hay=norm([item.data.title,...authorNames(item),sourceOf(item),doiOf(item),item.data.url,item.data.abstractNote,...tagsOf(item),...collectionNames(item)].join(' '));
  if(!criteria.words.every(w=>hay.includes(w)))return false;
  for(const [id,selected] of Object.entries(criteria.selected)){
    if(id!==ignore&&selected.length&&!selected.some(v=>valuesOf(item,id).includes(v)))return false;
  }
  return true;
}
function updateFacets(criteria) {
  for(const [id,config] of Object.entries(FILTERS)){
    const counts=new Map();
    for(const item of state.items.filter(i=>matches(i,criteria,id)))for(const value of valuesOf(item,id))counts.set(value,(counts.get(value)||0)+1);
    for(const option of Array.from($(id).options)){
      if(!option.value)continue;
      const n=counts.get(option.value)||0, selected=state.selected[id].includes(option.value);
      option.textContent=`${optionLabel(id,option.value)} (${n})`;
      option.disabled=config.multi&&selected || n===0&&!selected;
    }
  }
}
function searchUrl() {
  const url=new URL(location.href);url.search='';url.hash='';
  if($('search').value.trim())url.searchParams.set('q',$('search').value.trim());
  for(const [id,config] of Object.entries(FILTERS))for(const value of state.selected[id])url.searchParams.append(config.param,value);
  if($('yearFrom').value)url.searchParams.set('from',$('yearFrom').value);
  if($('yearTo').value)url.searchParams.set('to',$('yearTo').value);
  if($('sortOrder').value!=='newest')url.searchParams.set('sort',$('sortOrder').value);
  if($('resultView').value!=='table')url.searchParams.set('view',$('resultView').value);
  if($('groupYears').checked)url.searchParams.set('group','year');
  if(state.section!=='library')url.searchParams.set('section',state.section);
  if(state.section==='analysis'&&$('analysisCategory').value)url.searchParams.set('analysis_category',$('analysisCategory').value);
  return url.href;
}
function restoreSearch() {
  const params=new URL(location.href).searchParams;
  $('search').value=params.get('q')||'';
  for(const [id,config] of Object.entries(FILTERS)){
    const selected=params.getAll(config.param).map(v=>['taxonFilter','methodFilter','siteFilter'].includes(id)?LibraryModel.canonicalTag(({taxonFilter:'TAXON:',methodFilter:'METHOD:',siteFilter:'SITE:'}[id])+v).split(':').slice(1).join(':'):v).filter(v=>state.optionValues[id].includes(v));
    state.selected[id]=[...new Set(config.multi?selected:selected.slice(0,1))];
    if(!config.multi)$(id).value=state.selected[id][0]||'';
  }
  for(const [id,param] of [['yearFrom','from'],['yearTo','to']])$(''+id).value=/^\d{4}$/.test(params.get(param)||'')?params.get(param):'';
  $('sortOrder').value=['newest','oldest','title','author'].includes(params.get('sort'))?params.get('sort'):'newest';
  $('resultView').value=['cards','list','table'].includes(params.get('view'))?params.get('view'):'table';
  $('groupYears').checked=params.get('group')==='year';
  $('analysisCategory').value=['research','reports','datasets','other'].includes(params.get('analysis_category'))?params.get('analysis_category'):'';
  setSection(['analysis','quality'].includes(params.get('section'))?params.get('section'):'library');
}
function renderActiveFilters() {
  const buttons=[];
  const chip=(id,value,label)=>`<button type="button" class="filter-chip" data-filter="${esc(id)}" data-value="${esc(value)}" aria-label="${esc('Retirer '+label)}">${esc(label)} <span aria-hidden="true">×</span></button>`;
  if($('search').value.trim())buttons.push(chip('search','',`Recherche : ${$('search').value.trim()}`));
  for(const [id,config] of Object.entries(FILTERS))for(const value of state.selected[id])buttons.push(chip(id,value,`${config.label} : ${optionLabel(id,value)}`));
  if($('yearFrom').value)buttons.push(chip('yearFrom','','Depuis '+$('yearFrom').value));
  if($('yearTo').value)buttons.push(chip('yearTo','','Jusqu’à '+$('yearTo').value));
  $('activeFilters').innerHTML=buttons.join('');
}
function clearFilter(id, value='') {
  if(FILTERS[id]?.multi)state.selected[id]=state.selected[id].filter(v=>v!==value);
  else if(FILTERS[id]||['search','yearFrom','yearTo'].includes(id))$(id).value='';
  else return;
  applyFilters();
}

function updateStats() {
  const years = state.items.map(yearOf).filter(Boolean).map(Number);
  $("statTotal").textContent = state.items.length;
  $("statCore").textContent = state.items.filter(i=>tagsOf(i).includes("SCOPE:DSPA-Core")).length;
  $("statOpen").textContent = state.items.filter(i=>tagsOf(i).includes("ACCESS:Open")).length;
  $("statYears").textContent = years.length ? `${Math.min(...years)}–${Math.max(...years)}` : "—";
}

function applyFilters() {
  if(!state.ready)return;
  const criteria=currentCriteria(), sort=$('sortOrder').value;
  $('filterWarning').textContent=criteria.invalid?'Choisissez des années entre 1800 et 2100, avec un début antérieur ou égal à la fin.':'';
  state.filtered=state.items.filter(i=>matches(i,criteria)).sort((a,b)=>{
    const title=String(a.data.title).localeCompare(String(b.data.title),'fr');
    if(sort==='title')return title;
    if(sort==='author')return (authorSurnames(a)[0]||'').localeCompare(authorSurnames(b)[0]||'','fr')||title;
    const ya=yearOf(a),yb=yearOf(b);
    if(!ya||!yb)return ya?-1:yb?1:title;
    return (sort==='oldest'?Number(ya)-Number(yb):Number(yb)-Number(ya))||title;
  });
  updateFacets(criteria);renderActiveFilters();
  const url=searchUrl();$('searchLink').href=url;history.replaceState(null,'',url);
  $('shareStatus').textContent='';
  $('exportCsv').disabled=!(state.section==='library'?state.filtered:state.items).length;
  $('exportCsv').textContent=state.section==='library'?'Exporter les résultats en CSV':'Exporter la bibliothèque en CSV';
  render();
  if(typeof renderAnalytics==='function')renderAnalytics(state.items);
  if(typeof renderQuality==='function')renderQuality(state.items);
}

function setSection(section) {
  state.section=section;
  for(const name of ['library','analysis','quality']){
    $(name+'Panel').hidden=name!==section;
    $(name+'Tab').setAttribute('aria-pressed',String(name===section));
  }
  $('searchPanel').hidden=section!=='library';
}

function render() {
  $("resultCount").textContent = `${state.filtered.length} résultat${state.filtered.length!==1?"s":""} sur ${state.items.length}`;
  const el=$("results");
  const view=$('resultView').value;
  el.className=`results view-${view}`;
  if (!state.filtered.length) {
    el.innerHTML='<div class="empty panel"><h2>Aucune référence ne correspond à ces critères.</h2><p>Retirez un filtre actif ci-dessus ou élargissez la période.</p></div>';
    return;
  }
  function card(item) {
    const tags=tagsOf(item);
    const doi=doiOf(item);
    const url=safeUrl(item.data.url);
    const displayTags = tags.filter(t => view==='list'?t.startsWith('SCOPE:')||t.startsWith('ACCESS:'):!t.startsWith("STATUS:") && !t.startsWith("SYSTEM:"));
    const badges = displayTags.map(t => {
      const cls=t.startsWith("SCOPE:")?"scope":t==="ACCESS:Open"?"open":"";
      return `<span class="badge ${cls}">${esc(t)}</span>`;
    }).join("");
    return `<article class="card">
      <div class="card-top">
        <h2>${titleLink(item)}</h2>
        <div class="year">${esc(yearOf(item))}</div>
      </div>
      <p class="authors">${esc(authorsOf(item))}</p>
      <p class="source">${esc(sourceOf(item))}</p>
      <p class="document-type">${esc(TYPE_LABELS[item.data.itemType]||item.data.itemType)}</p>
      <div class="badges">${badges}</div>
      <div class="links">
        <a href="${esc(canonicalUrl(item))}" target="_blank" rel="noopener">Zotero</a>
        ${doi ? `<a href="https://doi.org/${encodeURIComponent(doi)}" target="_blank" rel="noopener">DOI</a>` : ""}
        ${url && !url.includes("doi.org") ? `<a href="${esc(url)}" target="_blank" rel="noopener">Lien</a>` : ""}
      </div>
    </article>`;
  }
  function table(items) {
    const rows=items.map(item=>{
      const tags=tagsOf(item),doi=doiOf(item);
      return `<tr><th scope="row">${titleLink(item)}<a class="table-zotero" href="${esc(canonicalUrl(item))}" target="_blank" rel="noopener">Notice Zotero</a></th><td>${esc(yearOf(item)||'Non renseignée')}</td><td>${esc(authorsOf(item))}</td><td>${esc(TYPE_LABELS[item.data.itemType]||item.data.itemType)}</td><td>${esc(tagValues(tags,'SCOPE:').join(', ')||'Non renseignée')}</td><td>${esc(tagValues(tags,'ACCESS:').map(v=>({Open:'Ouvert',Restricted:'Restreint'}[v]||v)).join(', ')||'Non renseigné')}</td></tr>`;
    }).join('');
    return `<div class="table-scroll" tabindex="0" role="region" aria-label="Tableau des références, défilement horizontal"><table class="reference-table"><caption>Comparaison des références · le titre ouvre la publication lorsqu'un DOI ou un lien est disponible.</caption><thead><tr><th scope="col">Titre · publication</th><th scope="col">Année</th><th scope="col">Auteurs</th><th scope="col">Type</th><th scope="col">Portée</th><th scope="col">Accès</th></tr></thead><tbody>${rows}</tbody></table></div>`;
  }
  const content=items=>view==='table'?table(items):items.map(card).join('');
  if(!$('groupYears').checked){el.innerHTML=content(state.filtered);return;}
  const groups=new Map();
  for(const item of state.filtered){const year=yearOf(item)||'Non renseignée';if(!groups.has(year))groups.set(year,[]);groups.get(year).push(item);}
  const years=[...groups.keys()].sort((a,b)=>a==='Non renseignée'?1:b==='Non renseignée'?-1:$('sortOrder').value==='oldest'?Number(a)-Number(b):Number(b)-Number(a));
  el.innerHTML=years.map(year=>`<section class="year-group" aria-label="${esc('Année '+year)}"><h2 class="year-heading">${esc(year)} <span>${groups.get(year).length} référence${groups.get(year).length>1?'s':''}</span></h2><div class="year-results">${content(groups.get(year))}</div></section>`).join('');
}

function csvCell(v) {
  let s=String(v??"");
  if (/^[\s]*[=+@-]/.test(s)) s="'"+s;
  return `"${s.replace(/"/g,'""')}"`;
}
function exportCsv() {
  const rows=[["Title","Authors","Year","Document type","Source","DOI","Collections","Tags","Zotero URL"]];
  for (const i of state.section==='library'?state.filtered:state.items) rows.push([
    i.data.title,authorNames(i).join('; '),yearOf(i),TYPE_LABELS[i.data.itemType]||i.data.itemType,sourceOf(i),doiOf(i),
    collectionNames(i).join("; "),tagsOf(i).join("; "),canonicalUrl(i)
  ]);
  const csv="\ufeff"+rows.map(r=>r.map(csvCell).join(",")).join("\r\n");
  const a=document.createElement("a");
  a.href=URL.createObjectURL(new Blob([csv],{type:"text/csv;charset=utf-8"}));
  a.download="dzanga_sangha_research_library.csv"; a.click();
  setTimeout(()=>URL.revokeObjectURL(a.href),1000);
}

async function init() {
  try {
    $("status").textContent="Chargement des collections…";
    const cols=await fetchAll(`${API}/collections`);
    cols.forEach(c=>state.collections.set(c.key,c.data.name));

    $("status").textContent="Chargement des références…";
    const raw=await fetchAll(`${API}/items/top?format=json`);
    state.items=raw.filter(i=>!["note","attachment","annotation"].includes(i.data.itemType));

    updateStats(); populateFilters();restoreSearch();state.ready=true;
    for(const section of ['library','analysis','quality'])$(section+'Tab').disabled=false;
    applyFilters();
    $("status").style.display="none";
  } catch (e) {
    console.error(e);
    $("status").innerHTML=`Impossible de charger la bibliothèque publique Zotero. L'administrateur doit autoriser la lecture publique du groupe dans Zotero. <small>${esc(e.message)}</small>`;
  }
}
["search",...Object.keys(FILTERS),"yearFrom","yearTo","sortOrder","resultView","groupYears"]
  .forEach(id=>$(id).addEventListener(["search","yearFrom","yearTo"].includes(id)?"input":"change",applyFilters));
$("resetFilters").addEventListener("click",()=>{
  $("search").value="";
  Object.keys(FILTERS).forEach(id=>{$(id).value="";state.selected[id]=[];});
  $('yearFrom').value='';$('yearTo').value='';$('sortOrder').value='newest';
  applyFilters();
});
$('activeFilters').addEventListener('click',e=>{const button=e.target.closest('button[data-filter]');if(button){const id=button.dataset.filter;clearFilter(id,button.dataset.value);$(id).focus();}});
$('copySearch').addEventListener('click',async()=>{
  try{await navigator.clipboard.writeText(searchUrl());$('shareStatus').textContent='Lien copié. Il conserve tous vos critères.';}
  catch{$('shareStatus').textContent='Copie indisponible : utilisez le lien de cette recherche pour copier son adresse.';}
});
window.addEventListener('popstate',()=>{if(state.ready){restoreSearch();applyFilters();}});
$("exportCsv").addEventListener("click",exportCsv);
$('libraryTab').addEventListener('click',()=>{setSection('library');applyFilters();});
$('analysisTab').addEventListener('click',()=>{setSection('analysis');applyFilters();});
$('qualityTab').addEventListener('click',()=>{setSection('quality');applyFilters();});
$('qualityIssue').addEventListener('change',()=>renderQuality(state.items));
$('qualityExport').addEventListener('click',exportQualityCsv);
$('analysisCategory').addEventListener('change',applyFilters);
$('browseDatasets').addEventListener('click',()=>{
  $('resetFilters').click();$('typeFilter').value='dataset';setSection('library');applyFilters();
  $('results').scrollIntoView({behavior:'smooth',block:'start'});
});
for(const section of ['library','analysis','quality'])$(section+'Tab').disabled=true;
const initialSection=new URL(location.href).searchParams.get('section');
setSection(['analysis','quality'].includes(initialSection)?initialSection:'library');
init();
