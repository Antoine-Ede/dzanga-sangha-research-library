const GROUP_ID = "6701789";
const API = `https://api.zotero.org/groups/${GROUP_ID}`;
const state = { items: [], collections: new Map(), filtered: [] };

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
  return (item.data.tags || []).map(x => x.tag).filter(Boolean);
}
function yearOf(item) {
  const m = String(item.data.date || "").match(/\b(18|19|20)\d{2}\b/);
  return m ? m[0] : "";
}
function authorsOf(item) {
  const cs = (item.data.creators || []).filter(c => ["author","editor"].includes(c.creatorType));
  const names = cs.map(c => c.name || [c.firstName,c.lastName].filter(Boolean).join(" "));
  if (names.length <= 4) return names.join(", ");
  return `${names.slice(0,3).join(", ")} et al.`;
}
function sourceOf(item) {
  return item.data.publicationTitle || item.data.bookTitle || item.data.proceedingsTitle ||
         item.data.publisher || item.data.institution || item.data.university || "";
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

function addOptions(id, values) {
  const select = $(id);
  [...new Set(values.filter(Boolean))].sort((a,b)=>b.localeCompare(a,undefined,{numeric:true})).forEach(v => {
    const o=document.createElement("option"); o.value=v; o.textContent=v; select.appendChild(o);
  });
}

function populateFilters() {
  addOptions("collectionFilter", [...state.collections.values()].filter(x => !/^00 |^99 /.test(x)));
  const allTags = state.items.flatMap(tagsOf);
  addOptions("scopeFilter", tagValues(allTags,"SCOPE:"));
  addOptions("siteFilter", tagValues(allTags,"SITE:"));
  addOptions("taxonFilter", tagValues(allTags,"TAXON:"));
  addOptions("methodFilter", tagValues(allTags,"METHOD:"));
  addOptions("accessFilter", tagValues(allTags,"ACCESS:"));
  addOptions("yearFilter", state.items.map(yearOf));
}

function updateStats() {
  const years = state.items.map(yearOf).filter(Boolean).map(Number);
  $("statTotal").textContent = state.items.length;
  $("statCore").textContent = state.items.filter(i=>tagsOf(i).includes("SCOPE:DSPA-Core")).length;
  $("statOpen").textContent = state.items.filter(i=>tagsOf(i).includes("ACCESS:Open")).length;
  $("statYears").textContent = years.length ? `${Math.min(...years)}–${Math.max(...years)}` : "—";
}

function applyFilters() {
  const q=norm($("search").value);
  const cf=$("collectionFilter").value;
  const sf=$("scopeFilter").value;
  const site=$("siteFilter").value;
  const tax=$("taxonFilter").value;
  const meth=$("methodFilter").value;
  const acc=$("accessFilter").value;
  const year=$("yearFilter").value;

  state.filtered = state.items.filter(item => {
    const tags=tagsOf(item);
    const hay=norm([
      item.data.title, authorsOf(item), sourceOf(item), doiOf(item), item.data.url,
      ...tags, ...collectionNames(item)
    ].join(" "));
    if (q && !hay.includes(q)) return false;
    if (cf && !collectionNames(item).includes(cf)) return false;
    if (sf && !tags.includes(`SCOPE:${sf}`)) return false;
    if (site && !tags.includes(`SITE:${site}`)) return false;
    if (tax && !tags.includes(`TAXON:${tax}`)) return false;
    if (meth && !tags.includes(`METHOD:${meth}`)) return false;
    if (acc && !tags.includes(`ACCESS:${acc}`)) return false;
    if (year && yearOf(item)!==year) return false;
    return true;
  }).sort((a,b) => (yearOf(b)||"0").localeCompare(yearOf(a)||"0") || String(a.data.title).localeCompare(String(b.data.title)));

  render();
}

function render() {
  $("resultCount").textContent = `${state.filtered.length} résultat${state.filtered.length!==1?"s":""}`;
  const el=$("results");
  if (!state.filtered.length) {
    el.innerHTML='<div class="empty panel">Aucune référence ne correspond aux filtres.</div>';
    return;
  }
  el.innerHTML = state.filtered.map(item => {
    const tags=tagsOf(item);
    const doi=doiOf(item);
    const url=safeUrl(item.data.url);
    const displayTags = tags.filter(t => !t.startsWith("STATUS:") && !t.startsWith("SYSTEM:"));
    const badges = displayTags.map(t => {
      const cls=t.startsWith("SCOPE:")?"scope":t==="ACCESS:Open"?"open":"";
      return `<span class="badge ${cls}">${esc(t)}</span>`;
    }).join("");
    return `<article class="card">
      <div class="card-top">
        <h2>${esc(item.data.title || "(Sans titre)")}</h2>
        <div class="year">${esc(yearOf(item))}</div>
      </div>
      <p class="authors">${esc(authorsOf(item))}</p>
      <p class="source">${esc(sourceOf(item))}</p>
      <div class="badges">${badges}</div>
      <div class="links">
        <a href="${esc(canonicalUrl(item))}" target="_blank" rel="noopener">Zotero</a>
        ${doi ? `<a href="https://doi.org/${encodeURIComponent(doi)}" target="_blank" rel="noopener">DOI</a>` : ""}
        ${url && !url.includes("doi.org") ? `<a href="${esc(url)}" target="_blank" rel="noopener">Lien</a>` : ""}
      </div>
    </article>`;
  }).join("");
}

function csvCell(v) {
  let s=String(v??"");
  if (/^[\s]*[=+@-]/.test(s)) s="'"+s;
  return `"${s.replace(/"/g,'""')}"`;
}
function exportCsv() {
  const rows=[["Title","Authors","Year","Source","DOI","Collections","Tags","Zotero URL"]];
  for (const i of state.filtered) rows.push([
    i.data.title,authorsOf(i),yearOf(i),sourceOf(i),doiOf(i),
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

    updateStats(); populateFilters();
    state.filtered=[...state.items]; applyFilters();
    $("status").style.display="none";
    $("exportCsv").disabled=false;
  } catch (e) {
    console.error(e);
    $("status").innerHTML=`Impossible de charger la bibliothèque publique Zotero. L'administrateur doit autoriser la lecture publique du groupe dans Zotero. <small>${esc(e.message)}</small>`;
  }
}
["search","collectionFilter","scopeFilter","siteFilter","taxonFilter","methodFilter","accessFilter","yearFilter"]
  .forEach(id=>$(id).addEventListener(id==="search"?"input":"change",applyFilters));
$("resetFilters").addEventListener("click",()=>{
  $("search").value="";
  ["collectionFilter","scopeFilter","siteFilter","taxonFilter","methodFilter","accessFilter","yearFilter"].forEach(id=>$(id).value="");
  applyFilters();
});
$("exportCsv").addEventListener("click",exportCsv);
init();
