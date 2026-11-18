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
  const core=items.filter(i=>tagsOf(i).includes('SCOPE:DSPA-Core')).length;
  const open=items.filter(i=>tagsOf(i).includes('ACCESS:Open')).length;
  return {total:items.length,documents:documents.length,datasets:items.length-documents.length,undated:documents.length-years.length,dated:years.length,core,open,timeline,
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
function analysisInsight(m) {
  const observed=m.timeline.filter(([,count])=>count>0);
  if(!observed.length)return 'Aucune tendance chronologique ne peut être calculée tant que le corpus sélectionné ne contient pas de document daté.';
  const [peakYear,peakCount]=observed.reduce((best,row)=>row[1]>best[1]?row:best,observed[0]);
  const latestYear=observed[observed.length-1][0];
  const coreShare=m.total?Math.round(m.core/m.total*100):0;
  return `Pic documentaire : ${peakYear} (${peakCount} document${peakCount>1?'s':''}). Dernière année renseignée : ${latestYear}. ${m.core} notice${m.core>1?'s':''} DSPA-Core (${coreShare} % du corpus sélectionné).`;
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
  $('analysisCount').textContent=`${m.total} références sélectionnées sur ${state.items.length}. Communication incluse ; ${m.undated} documents sans année.`;
  $('analysisInsight').textContent=analysisInsight(m);
  $('analysisSummary').innerHTML=[['Documents',m.documents],['Jeux de données',m.datasets],['DSPA-Core',m.core],['Avec année',m.dated]].map(([label,n])=>`<div><strong>${n}</strong><span>${label}</span></div>`).join('');
  $('themeAnalysis').innerHTML=analysisBars(m.themes,m.documents,v=>v.replace(/^\d+ - /,''));
  $('authorAnalysis').innerHTML=analysisBars(m.authors.slice(0,10),m.documents,v=>m.authorLabels[v]||v);
  $('typeAnalysis').innerHTML=analysisBars(m.types,m.total);
  $('scopeAnalysis').innerHTML=analysisBars(m.scope,m.total);
  $('accessAnalysis').innerHTML=analysisBars(m.access,m.total);
  $('siteAnalysis').innerHTML=analysisBars(m.sites,m.total);
  $('metadataAnalysis').innerHTML=analysisBars(m.metadata,m.total);
  renderStackedTimeline(items);
  renderPublisherAnalysis(items.filter(LibraryModel.isCommunication));
}
const CHART_COLORS=['#0072b2','#009e73','#d55e00'];
const TIMELINE_CLASSES=['research','communication','reports'];
const TIMELINE_LABELS={research:'Publications scientifiques',communication:'Communication',reports:'Rapports'};
function renderStackedTimeline(items) {
  const excluded=items.filter(i=>!TIMELINE_CLASSES.includes(LibraryModel.category(i))).length;
  items=items.filter(i=>TIMELINE_CLASSES.includes(LibraryModel.category(i)));
  const types=TIMELINE_CLASSES;
  const years=items.map(yearOf).filter(Boolean).map(Number);
  if(!years.length){$('publicationTimeline').innerHTML='<p>Aucune référence datée.</p>';return;}
  const rows=Array.from({length:Math.max(...years)-Math.min(...years)+1},(_,n)=>{
    const year=String(Math.min(...years)+n);
    const counts=types.map(type=>items.filter(i=>yearOf(i)===year&&LibraryModel.category(i)===type).length);
    return {year,counts,total:counts.reduce((a,b)=>a+b,0)};
  });
  const peak=Math.max(1,...rows.map(r=>r.total));
  const label=type=>TIMELINE_LABELS[type];
  $('publicationTimeline').innerHTML=
    '<p>Total annuel des trois classes : publications scientifiques, communication et rapports. '+excluded+' notices hors de ces classes (dont données et documents non classés) exclues ; les notices sans année ne sont pas représentées.</p>'+
    '<ul class="chart-legend">'+types.map((type,n)=>'<li><span style="background:'+CHART_COLORS[n%CHART_COLORS.length]+'"></span>'+esc(label(type))+'</li>').join('')+'</ul>'+
    '<div class="timeline-scroll"><div class="timeline" style="--year-count:'+rows.length+'">'+rows.map(({year,counts,total},n)=>{
      const detail=counts.map((count,k)=>count?label(types[k])+': '+count:'').filter(Boolean).join(', ');
      return '<button class="year-bar" type="button" data-analysis-year="'+year+'" aria-label="'+esc(year+' : '+total+' références. '+detail)+'" title="'+esc(year+' — '+detail)+'"><span class="bar-count">'+total+'</span><span class="year-column stacked" style="height:'+total/peak*145+'px" aria-hidden="true">'+counts.map((count,k)=>count?'<span style="height:'+count/total*100+'%;background:'+CHART_COLORS[k%CHART_COLORS.length]+'"></span>':'').join('')+'</span><span class="year-tick">'+(n===0||n===rows.length-1||Number(year)%5===0?year:'·')+'</span></button>';
    }).join('')+'</div></div><details class="chart-data"><summary>Valeurs par année, par classe et total</summary><div class="table-scroll"><table><caption>Nombre de notices datées</caption><thead><tr><th>Année</th>'+types.map(t=>'<th>'+esc(label(t))+'</th>').join('')+'<th>Total</th></tr></thead><tbody>'+rows.map(r=>'<tr><th scope="row">'+r.year+'</th>'+r.counts.map(n=>'<td>'+n+'</td>').join('')+'<td>'+r.total+'</td></tr>').join('')+'</tbody></table></div></details>';
}
function renderPublisherAnalysis(items) {
  const sources = new Map();
  let missing = 0;
  for (const item of items) {
    const source = mediaSource(item).trim();
    if (!source) {
      missing++;
      continue;
    }
    sources.set(source, (sources.get(source) || 0) + 1);
  }
  const ranked = [...sources].sort((a, b) => b[1] - a[1] || a[0].localeCompare(b[0], 'fr'));
  $('publisherAnalysis').innerHTML = analysisBars(ranked.slice(0, 15), items.length);
  $('publisherCoverage').textContent = items.length
    ? `${items.length - missing} contenus avec source renseignée sur ${items.length}.`
    : 'Aucun contenu Communication dans cette sélection.';
}
document.getElementById('publicationTimeline').addEventListener('click',event=>{
  const button=event.target.closest('button[data-analysis-year]');if(!button)return;
  const category = $('analysisCategory').value;
  if (category === 'communication') {
    setSection('communication');
    $('communicationSearch').value = '';
    for (const id of Object.keys(COMMUNICATION_FILTERS)) $(id).value = '';
    $('communicationYear').value = button.dataset.analysisYear;
    applyFilters();
    $('communicationYear').focus();
    return;
  }
  setSection(category==='research'?'library':category==='reports'?'reports':'browse');
  document.getElementById('resetFilters').click();
  document.getElementById('categoryFilter').value=document.getElementById('analysisCategory').value;
  document.getElementById('yearFilter').value='';
  document.getElementById('yearFrom').value=button.dataset.analysisYear;
  document.getElementById('yearTo').value=button.dataset.analysisYear;applyFilters();
  document.getElementById('yearFilter').focus();
});
