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
  renderMediaGeography(items.filter(LibraryModel.isCommunication));
}
const CHART_COLORS=['#0072b2','#d55e00','#009e73','#cc79a7','#806300','#564a9b','#474747','#56b4e9','#8a4f20','#24847c','#a73866','#666f26'];
function renderStackedTimeline(items) {
  const types=[...new Set(items.map(i=>i.data.itemType))].sort();
  const years=items.map(yearOf).filter(Boolean).map(Number);
  if(!years.length){$('publicationTimeline').innerHTML='<p>Aucune référence datée.</p>';return;}
  const rows=Array.from({length:Math.max(...years)-Math.min(...years)+1},(_,n)=>{
    const year=String(Math.min(...years)+n);
    const counts=types.map(type=>items.filter(i=>yearOf(i)===year&&i.data.itemType===type).length);
    return {year,counts,total:counts.reduce((a,b)=>a+b,0)};
  });
  const peak=Math.max(1,...rows.map(r=>r.total));
  const label=type=>TYPE_LABELS[type]||type;
  $('publicationTimeline').innerHTML=
    '<p>Nombre de références par année — hauteur totale et répartition par type. Les notices sans année sont exclues du graphique.</p>'+
    '<ul class="chart-legend">'+types.map((type,n)=>'<li><span style="background:'+CHART_COLORS[n%CHART_COLORS.length]+'"></span>'+esc(label(type))+'</li>').join('')+'</ul>'+
    '<div class="timeline-scroll"><div class="timeline" style="--year-count:'+rows.length+'">'+rows.map(({year,counts,total},n)=>{
      const detail=counts.map((count,k)=>count?label(types[k])+': '+count:'').filter(Boolean).join(', ');
      return '<button class="year-bar" type="button" data-analysis-year="'+year+'" aria-label="'+esc(year+' : '+total+' références. '+detail)+'" title="'+esc(year+' — '+detail)+'"><span class="bar-count">'+total+'</span><span class="year-column stacked" style="height:'+total/peak*145+'px" aria-hidden="true">'+counts.map((count,k)=>count?'<span style="height:'+count/total*100+'%;background:'+CHART_COLORS[k%CHART_COLORS.length]+'"></span>':'').join('')+'</span><span class="year-tick">'+(n===0||n===rows.length-1||Number(year)%5===0?year:'·')+'</span></button>';
    }).join('')+'</div></div><details class="chart-data"><summary>Valeurs par année, par type et total</summary><div class="table-scroll"><table><caption>Nombre de notices datées</caption><thead><tr><th>Année</th>'+types.map(t=>'<th>'+esc(label(t))+'</th>').join('')+'<th>Total</th></tr></thead><tbody>'+rows.map(r=>'<tr><th scope="row">'+r.year+'</th>'+r.counts.map(n=>'<td>'+n+'</td>').join('')+'<td>'+r.total+'</td></tr>').join('')+'</tbody></table></div></details>';
}
// Explicit country metadata only. Coordinates are approximate country centres.
const MEDIA_COUNTRIES={
  FR:['France',2,47],DE:['Allemagne',10,51],ES:['Espagne',-4,40],GB:['Royaume-Uni',-2,54],
  US:['États-Unis',-98,39],CA:['Canada',-106,56],BE:['Belgique',4,51],CH:['Suisse',8,47],
  CF:['République centrafricaine',21,7],CG:['République du Congo',15,-1],CM:['Cameroun',12,6],
  NL:['Pays-Bas',5,52],IT:['Italie',12,43],CZ:['Tchéquie',15,50],AU:['Australie',134,-25],
  ZA:['Afrique du Sud',25,-29],JP:['Japon',138,37],BR:['Brésil',-52,-14]
};
function mediaCountry(item){
  const values=tagsOf(item).filter(t=>t.startsWith('PUBLISHER-COUNTRY:')).map(t=>t.slice(18));
  const extra=String(item.data.extra||'').match(/^Publisher country:\s*(.+)$/im);
  if(extra)values.push(extra[1].trim());
  const unique=[...new Set(values.map(v=>v.trim()).filter(Boolean))];
  if(unique.length!==1)return '';
  const value=unique[0];
  return Object.keys(MEDIA_COUNTRIES).find(code=>code===value.toUpperCase()||norm(MEDIA_COUNTRIES[code][0])===norm(value))||value;
}
function renderMediaGeography(items){
  const countries=new Map(),sources=new Map();
  for(const item of items){
    const country=mediaCountry(item)||'Non renseigné';
    countries.set(country,(countries.get(country)||0)+1);
    const source=mediaSource(item).trim()||'Source non renseignée';
    sources.set(source,(sources.get(source)||0)+1);
  }
  const sorted=m=>[...m].sort((a,b)=>b[1]-a[1]||a[0].localeCompare(b[0],'fr'));
  const located=items.filter(i=>MEDIA_COUNTRIES[mediaCountry(i)]).length;
  $('countryCoverage').textContent=located+' notices localisées sur '+items.length+'. '+(countries.get('Non renseigné')||0)+' sans pays explicite. Carte schématique ; les valeurs exactes figurent ci-dessous.';
  $('countryAnalysis').innerHTML=analysisBars(sorted(countries),items.length,c=>MEDIA_COUNTRIES[c]?.[0]||c);
  $('publisherAnalysis').innerHTML=analysisBars(sorted(sources).slice(0,15),items.length);
  const x=lon=>(lon+180)*2,y=lat=>(90-lat)*2;
  // Generalised continental silhouettes for orientation, not political boundaries.
  const land=[
    [[-168,70],[-130,70],[-100,82],[-55,52],[-80,25],[-98,15],[-117,32],[-130,55]],
    [[-81,12],[-50,5],[-35,-7],[-50,-30],[-68,-55],[-76,-20]],
    [[-55,60],[-20,75],[-42,83],[-60,76]],
    [[-17,36],[10,37],[35,30],[51,12],[40,-15],[18,-35],[8,-5],[-17,15]],
    [[-10,36],[-10,60],[25,71],[60,70],[110,75],[180,65],[145,40],[120,20],[105,-5],[80,8],[55,25],[35,30],[25,40]],
    [[112,-12],[137,-10],[153,-25],[145,-39],[115,-35]],
    [[166,-34],[179,-40],[170,-47]]
  ].map(points=>'<polygon points="'+points.map(([lon,lat])=>x(lon)+','+y(lat)).join(' ')+'"/>').join('');
  const grid=[-120,-60,0,60,120].map(l=>'<path d="M '+x(l)+' 0 V 360"/>').join('')+[-60,-30,0,30,60].map(l=>'<path d="M 0 '+y(l)+' H 720"/>').join('');
  const dots=sorted(countries).filter(([code])=>MEDIA_COUNTRIES[code]).map(([code,n])=>{
    const [name,lon,lat]=MEDIA_COUNTRIES[code];
    return '<g><title>'+esc(name+': '+n+' notices')+'</title><circle cx="'+x(lon)+'" cy="'+y(lat)+'" r="'+(4+Math.sqrt(n)*3)+'"/><text x="'+(x(lon)+8)+'" y="'+(y(lat)-8)+'">'+esc(code)+'</text></g>';
  }).join('');
  $('communicationMap').innerHTML='<svg class="country-map" viewBox="0 0 720 360" role="img" aria-label="Carte schématique des pays des médias, projection longitude latitude ; valeurs dans la liste des pays"><rect width="720" height="360" fill="#eef3f5"/><g fill="#d3dfd3" stroke="#abbcab">'+land+'</g><g stroke="#c9d6dc" fill="none">'+grid+'</g><g fill="#0072b2" fill-opacity=".65" stroke="#183126">'+dots+'</g><text x="8" y="20">90° N</text><text x="8" y="350">90° S</text><text x="340" y="350">0°</text></svg>';
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
