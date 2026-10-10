/* Shared curation rules. No inference of scientific scope or access rights. */
(function(root){
  const aliases={'TAXON:Elephant':'TAXON:Elephants','TAXON:Gorillas':'TAXON:Gorilla','METHOD:Behavioral-observation':'METHOD:Behavioural-observation','SITE:Bai Hokou':'SITE:Bai-Hokou','SITE:Bai-Hoköu':'SITE:Bai-Hokou','SITE:Dzanga Sangha':'SITE:Dzanga-Sangha'};
  const labels={research:'Publications scientifiques et thèses',reports:'Rapports, gestion et développement',datasets:'Jeux de données et protocoles',other:'Autres documents'};
  function canonicalTag(tag){return aliases[tag]||tag;}
  function tags(item){return [...new Set((item.data.tags||[]).map(t=>canonicalTag(t.tag)).filter(Boolean))];}
  function category(item){const type=item.data.itemType;if(type==='dataset')return 'datasets';if(type==='report')return 'reports';if(['journalArticle','thesis','book','bookSection','conferencePaper','preprint'].includes(type))return 'research';return 'other';}
  function authorKey(c){return (c.name||[c.firstName,c.lastName].filter(Boolean).join(' ')).normalize('NFD').replace(/[\u0300-\u036f]/g,'').toLowerCase().trim().replace(/\s+/g,' ');}
  function issues(item){
    const d=item.data,t=tags(item),out=[];
    if(!String(d.title||'').trim())out.push('Titre manquant');
    if(!/\b(?:18|19|20)\d{2}\b/.test(d.date||''))out.push('Année manquante');
    if(!(d.creators||[]).some(c=>['author','editor'].includes(c.creatorType)&&(c.name||c.lastName)))out.push('Auteur ou responsable manquant');
    if(![d.publicationTitle,d.bookTitle,d.proceedingsTitle,d.publisher,d.institution,d.university,d.repository].some(v=>String(v||'').trim()))out.push('Source bibliographique manquante');
    if(t.filter(v=>/^SCOPE:DSPA-(Core|Relevant)$/.test(v)).length!==1)out.push('Portée à préciser');
    if(t.includes('SCOPE:DSPA-Core')&&!/(?:scope evidence|classification evidence(?:\s*\([^)]*\))?|evidence|preuve|justification)\s*:\s*\S.{10}/i.test(d.extra||''))out.push('Justification Core à expliciter');
    if(t.filter(v=>/^ACCESS:(Open|Restricted)$/.test(v)).length!==1)out.push('Accès à déterminer');
    if(t.includes('STATUS:Metadata-Incomplete')||t.includes('STATUS:To-Review'))out.push('Vérification signalée dans Zotero');
    const doi=String(d.DOI||'').trim()||String(d.extra||'').match(/^DOI:\s*(\S+)/im)?.[1];
    let url;try{url=new URL(d.url);}catch{}
    if(!doi&&!['http:','https:'].includes(url?.protocol))out.push('Lien externe non renseigné');
    return out;
  }
  const model={aliases,labels,canonicalTag,tags,category,authorKey,issues};
  if(typeof module!=='undefined'&&module.exports)module.exports=model;
  root.LibraryModel=model;
})(typeof globalThis==='undefined'?this:globalThis);
