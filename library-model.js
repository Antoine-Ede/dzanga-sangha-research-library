/* Shared curation rules. No inference of scientific scope or access rights. */
(function(root){
  const aliases={'TAXON:Elephant':'TAXON:Elephants','TAXON:Gorillas':'TAXON:Gorilla','METHOD:Behavioral-observation':'METHOD:Behavioural-observation','SITE:Bai Hokou':'SITE:Bai-Hokou','SITE:Bai-Hoköu':'SITE:Bai-Hokou','SITE:Dzanga Sangha':'SITE:Dzanga-Sangha'};
  const labels={research:'Publications scientifiques et thèses',reports:'Rapports, gestion et développement',datasets:'Jeux de données et protocoles',other:'Autres documents'};
  function canonicalTag(tag){return aliases[tag]||tag;}
  function tags(item){return [...new Set((item.data.tags||[]).map(t=>canonicalTag(t.tag)).filter(Boolean))];}
  function category(item){const type=item.data.itemType;if(type==='dataset')return 'datasets';if(type==='report')return 'reports';if(['journalArticle','thesis','book','bookSection','conferencePaper','preprint'].includes(type))return 'research';return 'other';}
  function authorKey(c){return (c.name||[c.firstName,c.lastName].filter(Boolean).join(' ')).normalize('NFD').replace(/[\u0300-\u036f]/g,'').toLowerCase().trim().replace(/\s+/g,' ');}
  // A review hint, never an automatic permutation or an identity decision.
  function authorNeedsReview(c){
    return !c.name && ['author','editor'].includes(c.creatorType) &&
      /^(?:[A-Z]\.?\s*){1,3}$/.test(String(c.lastName||'').trim()) &&
      /\p{L}{3}/u.test(String(c.firstName||''));
  }
  function archiveSummary(item){
    const d=item.data, extra=String(d.extra||''), t=tags(item);
    const gaps=[...extra.matchAll(/Informations manquantes(?: ou à confirmer)?\s*:\s*([^\r\n.]+[.]?)/gi)]
      .map(m=>m[1].trim()).filter(Boolean);
    return {
      gaps:[...new Set(gaps)],
      incomplete:t.includes('STATUS:Metadata-Incomplete'),
      sensitive:/Original contenant des éléments sensibles/i.test(extra),
      controlled:/consultation (?:encadrée|aux APDS)/i.test(extra)||t.includes('ACCESS:Restricted-Original'),
      restricted:t.includes('ACCESS:Restricted'),
      publicCopy:/version publique expurgée/i.test(extra),
      details:extra
    };
  }
  function issues(item){
    const d=item.data,t=tags(item),out=[];
    if(!String(d.title||'').trim())out.push('Titre manquant');
    if(!/\b(?:18|19|20)\d{2}\b/.test(d.date||''))out.push('Année manquante');
    if(!(d.creators||[]).some(c=>['author','editor'].includes(c.creatorType)&&(c.name||c.lastName)))out.push('Auteur ou responsable manquant');
    if((d.creators||[]).some(authorNeedsReview))out.push('Nom/prénom à vérifier : nom réduit à des initiales');
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
  const model={aliases,labels,canonicalTag,tags,category,authorKey,authorNeedsReview,archiveSummary,issues};
  if(typeof module!=='undefined'&&module.exports)module.exports=model;
  root.LibraryModel=model;
})(typeof globalThis==='undefined'?this:globalThis);
