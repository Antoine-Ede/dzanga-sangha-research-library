function qualityRows(items){return items.map(item=>({item,issues:LibraryModel.issues(item)})).filter(r=>r.issues.length);}
function renderQuality(items){
  const all=qualityRows(items),selected=$('qualityIssue').value;
  const reasons=[...new Set(all.flatMap(r=>r.issues))].sort((a,b)=>a.localeCompare(b,'fr'));
  $('qualityIssue').innerHTML='<option value="">Tous les points à vérifier</option>'+reasons.map(v=>`<option value="${esc(v)}"${v===selected?' selected':''}>${esc(v)} (${all.filter(r=>r.issues.includes(v)).length})</option>`).join('');
  const rows=selected?all.filter(r=>r.issues.includes(selected)):all;
  $('qualityCount').textContent=`${rows.length} notices à examiner sur ${items.length}. Ces indicateurs signalent des vérifications, pas une note de qualité scientifique.`;
  $('qualityExport').disabled=!rows.length;
  $('qualityResults').innerHTML=rows.length?`<div class="table-scroll" tabindex="0" role="region" aria-label="Tableau des vérifications bibliographiques"><table class="reference-table"><caption>Points à vérifier dans les notices Zotero</caption><thead><tr><th scope="col">Référence</th><th scope="col">Catégorie</th><th scope="col">Vérifications</th></tr></thead><tbody>${rows.map(r=>`<tr><th scope="row">${esc(r.item.data.title||'(Sans titre)')}<a class="table-zotero" href="${esc(canonicalUrl(r.item))}" target="_blank" rel="noopener">Examiner dans Zotero</a></th><td>${esc(LibraryModel.labels[LibraryModel.category(r.item)])}</td><td><ul>${r.issues.map(v=>`<li>${esc(v)}</li>`).join('')}</ul></td></tr>`).join('')}</tbody></table></div>`:'<p class="empty">Aucun point à vérifier selon ces critères.</p>';
}
function exportQualityCsv(){
  const selected=$('qualityIssue').value,rows=qualityRows(state.items).filter(r=>!selected||r.issues.includes(selected));
  const data=[['Titre','Catégorie','Vérifications','Zotero'],...rows.map(r=>[r.item.data.title,LibraryModel.labels[LibraryModel.category(r.item)],r.issues.join('; '),canonicalUrl(r.item)])];
  const a=document.createElement('a');a.href=URL.createObjectURL(new Blob(['\ufeff'+data.map(r=>r.map(csvCell).join(',')).join('\r\n')],{type:'text/csv;charset=utf-8'}));a.download='dzanga_sangha_verifications.csv';a.click();setTimeout(()=>URL.revokeObjectURL(a.href),1000);
}
