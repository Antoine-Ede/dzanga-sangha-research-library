// All indicators derive from public Zotero records; no stored corpus or private key.
function researchMetrics(items) {
  const documents=items.filter(i=>i.data.itemType!=='dataset');
  const countValues=(records,get)=>{
    const counts=new Map();for(const item of records)for(const value of new Set(get(item).filter(Boolean)))counts.set(value,(counts.get(value)||0)+1);
    return [...counts].sort((a,b)=>b[1]-a[1]||a[0].localeCompare(b[0],'fr'));
  };
  const years=documents.map(yearOf).filter(Boolean).map(Number);
  const allYears=items.map(yearOf).filter(Boolean).map(Number);
  const yearly=countValues(documents,i=>[yearOf(i)]),yearCounts=new Map(yearly);
  const timeline=years.length?Array.from({length:Math.max(...years)-Math.min(...years)+1},(_,n)=>{const y=String(Math.min(...years)+n);return [y,yearCounts.get(y)||0];}):[];
  return {total:items.length,documents:documents.length,datasets:items.length-documents.length,undated:documents.length-years.length,timeline,
    themes:countValues(documents,i=>collectionNames(i).filter(v=>!/^00 |^99 /.test(v))),
    authors:countValues(documents,i=>(i.data.creators||[]).filter(c=>c.creatorType==='author').map(LibraryModel.authorKey)),
    authorLabels:Object.fromEntries(documents.flatMap(i=>(i.data.creators||[]).filter(c=>c.creatorType==='author').map(c=>[LibraryModel.authorKey(c),c.name||[c.firstName,c.lastName].filter(Boolean).join(' ')]))),
    categories:countValues(items,i=>[LibraryModel.labels[LibraryModel.category(i)]]),
    yearCategories:allYears.length?Array.from({length:Math.max(...allYears)-Math.min(...allYears)+1},(_,n)=>String(Math.min(...allYears)+n)).map(year=>[year,...['research','reports','datasets','other'].map(cat=>items.filter(i=>yearOf(i)===year&&LibraryModel.category(i)===cat).length)]):[],
    types:countValues(items,i=>[TYPE_LABELS[i.data.itemType]||i.data.itemType]),
    scope:countValues(items,i=>tagValues(tagsOf(i),'SCOPE:').length?tagValues(tagsOf(i),'SCOPE:'):['Non renseignée']),
    access:countValues(items,i=>tagValues(tagsOf(i),'ACCESS:').length?tagValues(tagsOf(i),'ACCESS:').map(v=>({Open:'Ouvert',Restricted:'Restreint'}[v]||v)):['Non renseigné']),
    sites:countValues(items,i=>tagValues(tagsOf(i),'SITE:')),
    metadata:[['Titre',items.filter(i=>String(i.data.title||'').trim()).length],['Année',items.filter(yearOf).length],['Auteur',items.filter(i=>(i.data.creators||[]).some(c=>c.creatorType==='author'&&(c.lastName||c.name))).length],['DOI',items.filter(doiOf).length],['Site',items.filter(i=>tagValues(tagsOf(i),'SITE:').length).length]]};
}
function analysisBars(rows,total,label=v=>v) {
  if(!rows.length)return '<p class="analysis-empty">Aucune valeur renseignée dans cette sélection.</p>';
  return '<ul class="analysis-bars">'+rows.map(([value,count])=>{
    const percent=total?Math.round(count/total*100):0;
    return `<li><div class="bar-label"><span>${esc(label(value))}</span><strong>${count} <small>· ${percent} %</small></strong></div><div class="bar-track" aria-hidden="true"><span style="width:${Math.min(percent,100)}%"></span></div></li>`;
  }).join('')+'</ul>';
}
function renderAnalytics(items) {
  const category=$('analysisCategory').value;
  if(category)items=items.filter(i=>LibraryModel.category(i)===category);
  const m=researchMetrics(items);
  $('analysisCount').textContent=`${m.total} références sélectionnées sur ${state.items.length}.`;
  $('analysisSummary').innerHTML=[['Documents',m.documents],['Jeux de données',m.datasets],['Noms d’auteur',m.authors.length],['Documents sans date',m.undated]].map(([label,n])=>`<div><strong>${n}</strong><span>${label}</span></div>`).join('');
  const series=m.yearCategories.map(([year,...ns])=>[year,ns.reduce((a,b)=>a+b,0)]),peak=Math.max(1,...series.map(([,n])=>n));
  $('publicationTimeline').innerHTML=series.length?`<div class="timeline-scroll"><div class="timeline" style="--year-count:${series.length}">${series.map(([year,n],i)=>`<button class="year-bar" type="button" data-analysis-year="${year}" aria-label="${year} : ${n} documents, filtrer cette année"><span class="bar-count">${n}</span><span class="year-column" style="height:${n/peak*145}px" aria-hidden="true"></span><span class="year-tick">${i===0||i===series.length-1||Number(year)%5===0?year:'·'}</span></button>`).join('')}</div></div><details class="chart-data"><summary>Comparer les catégories par année</summary><div class="table-scroll"><table class="reference-table"><caption>Année de publication ; pour les données, année de la notice du dépôt</caption><thead><tr><th scope="col">Année</th><th scope="col">Publications et thèses</th><th scope="col">Rapports</th><th scope="col">Données et protocoles</th><th scope="col">Autres</th></tr></thead><tbody>${m.yearCategories.map(([y,...ns])=>`<tr><th scope="row">${y}</th>${ns.map(n=>`<td>${n}</td>`).join('')}</tr>`).join('')}</tbody></table></div></details>`:'<p>Aucun document daté dans cette sélection.</p>';
  $('themeAnalysis').innerHTML=analysisBars(m.themes,m.documents,v=>v.replace(/^\d+ - /,''));
  $('authorAnalysis').innerHTML=analysisBars(m.authors.slice(0,10),m.documents,v=>m.authorLabels[v]||v);
  $('typeAnalysis').innerHTML=analysisBars(m.types,m.total);
  $('scopeAnalysis').innerHTML=analysisBars(m.scope,m.total);
  $('accessAnalysis').innerHTML=analysisBars(m.access,m.total);
  $('siteAnalysis').innerHTML=analysisBars(m.sites,m.total);
  $('metadataAnalysis').innerHTML=analysisBars(m.metadata,m.total);
}
document.getElementById('publicationTimeline').addEventListener('click',event=>{
  const button=event.target.closest('button[data-analysis-year]');if(!button)return;
  setSection('library');document.getElementById('resetFilters').click();
  document.getElementById('categoryFilter').value=document.getElementById('analysisCategory').value;
  document.getElementById('yearFilter').value='';
  document.getElementById('yearFrom').value=button.dataset.analysisYear;
  document.getElementById('yearTo').value=button.dataset.analysisYear;applyFilters();
  document.getElementById('yearFilter').focus();
});
