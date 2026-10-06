// Citation snapshot uses public OpenAlex identifiers; bibliographic content stays in Zotero.
const publicationNetwork={data:null,loading:false,failed:false};
function networkModel(items,snapshot,mode='direct',minimum=2,focus='') {
  const documents=items.filter(i=>i.data.itemType!=='dataset');
  const current=new Map(documents.map(i=>[i.key,i]));
  const indexed=new Map((snapshot.nodes||[]).filter(n=>current.has(n.key)&&doiOf(current.get(n.key))===n.doi).map(n=>[n.key,n]));
  let links=(mode==='coupled'?snapshot.coupled:snapshot.direct)||[];
  links=links.filter(l=>indexed.has(l.source)&&indexed.has(l.target)&&l.source!==l.target&&(mode!=='coupled'||l.shared>=minimum));
  const connected=new Set(links.flatMap(l=>[l.source,l.target]));
  const fullLinks=links;
  if(focus)links=links.filter(l=>l.source===focus||l.target===focus);
  const available=links.length;
  // Restrict visual density only, retaining all relationships in the detail list.
  links=links.slice(0,focus?100:200);
  const visible=new Set(links.flatMap(l=>[l.source,l.target]));if(focus&&indexed.has(focus))visible.add(focus);
  return {documents,indexed,current,connected,fullLinks,links,available,nodes:[...visible].sort().map(key=>current.get(key))};
}
function networkPositions(nodes,links) {
  const positions=new Map(nodes.map((n,i)=>[n.key,{x:450+300*Math.cos(i*2*Math.PI/nodes.length),y:280+215*Math.sin(i*2*Math.PI/nodes.length)}]));
  // Deterministic bounded force layout; no animations or physics loops after render.
  for(let t=0;t<65;t++){
    const forces=new Map(nodes.map(n=>[n.key,{x:0,y:0}]));
    for(let a=0;a<nodes.length;a++)for(let b=a+1;b<nodes.length;b++){
      const p=positions.get(nodes[a].key),q=positions.get(nodes[b].key),dx=p.x-q.x,dy=p.y-q.y,d=Math.max(12,Math.hypot(dx,dy)),f=Math.min(6,2200/(d*d));
      forces.get(nodes[a].key).x+=dx/d*f;forces.get(nodes[a].key).y+=dy/d*f;forces.get(nodes[b].key).x-=dx/d*f;forces.get(nodes[b].key).y-=dy/d*f;
    }
    for(const l of links){const p=positions.get(l.source),q=positions.get(l.target),dx=q.x-p.x,dy=q.y-p.y,d=Math.max(1,Math.hypot(dx,dy)),f=(d-85)*.014;forces.get(l.source).x+=dx/d*f;forces.get(l.source).y+=dy/d*f;forces.get(l.target).x-=dx/d*f;forces.get(l.target).y-=dy/d*f;}
    for(const n of nodes){const p=positions.get(n.key),f=forces.get(n.key);p.x=Math.max(24,Math.min(876,p.x+f.x+(450-p.x)*.003));p.y=Math.max(24,Math.min(536,p.y+f.y+(280-p.y)*.003));}
  }
  return positions;
}
async function loadPublicationNetwork() {
  if(publicationNetwork.loading)return;
  if(publicationNetwork.data){renderPublicationNetwork();return;}
  if(publicationNetwork.failed)return;
  publicationNetwork.loading=true;$('networkStatus').textContent='Chargement des liens bibliographiques…';
  try{
    const response=await fetch('assets/publication-network.json?v=20261006-network',{signal:AbortSignal.timeout(30000)});
    if(!response.ok)throw new Error('Snapshot HTTP '+response.status);
    const data=await response.json();
    if(data.schemaVersion!==1||!Array.isArray(data.nodes)||!Array.isArray(data.direct)||!Array.isArray(data.coupled))throw new Error('Snapshot invalide');
    publicationNetwork.data=data;
    const m=networkModel(state.items,data),options=[...m.indexed.keys()].map(key=>m.current.get(key)).sort((a,b)=>String(a.data.title).localeCompare(String(b.data.title),'fr'));
    for(const item of options){const option=document.createElement('option');option.value=item.key;option.textContent=`${yearOf(item)||'Sans date'} · ${item.data.title}`;$('networkFocus').appendChild(option);}
    $('networkControls').hidden=false;renderPublicationNetwork();
  }catch(e){publicationNetwork.failed=true;$('networkStatus').textContent='Le réseau est indisponible. Actualisez la page pour réessayer ; la bibliothèque reste accessible.';}
  finally{publicationNetwork.loading=false;}
}
function renderPublicationNetwork() {
  const data=publicationNetwork.data;if(!data)return;
  const mode=$('networkMode').value||'direct',minimum=Number($('networkThreshold').value)||2,focus=$('networkFocus').value;
  const m=networkModel(state.items,data,mode,minimum,focus);
  $('networkThresholdLabel').hidden=mode!=='coupled';
  $('networkStatus').textContent=`OpenAlex · relevé du ${new Date(data.generatedAt).toLocaleDateString('fr-FR',{timeZone:'Africa/Bangui'})} · ${m.indexed.size}/${m.documents.length} documents retrouvés par DOI ; ${[...m.indexed.values()].filter(n=>n.referenceCount>0).length} avec références indexées.`;
  $('networkExplanation').textContent=mode==='direct'?'La flèche va du document qui cite vers le document cité. Seuls les liens entre documents présents dans Zotero sont représentés.':'Deux documents sont reliés lorsqu’ils citent au moins '+minimum+' références communes, y compris des références extérieures à Zotero. Ce couplage bibliographique indique une proximité, sans prouver qu’ils se citent. Les liens sont classés par proportion de références communes (normalisation cosinus).';
  $('networkCount').textContent=`${m.nodes.length} document${m.nodes.length!==1?'s':''} affiché${m.nodes.length!==1?'s':''} · ${m.links.length} lien${m.links.length!==1?'s':''} représenté${m.links.length!==1?'s':''} sur ${m.available}${m.available>m.links.length?' · affichage limité pour rester lisible ; sélectionnez un document pour explorer son voisinage.':'.'}`;
  const positions=networkPositions(m.nodes,m.links);
  const lines=m.links.map(l=>{const p=positions.get(l.source),q=positions.get(l.target),dx=q.x-p.x,dy=q.y-p.y,d=Math.max(1,Math.hypot(dx,dy));return `<line x1="${p.x+dx/d*9}" y1="${p.y+dy/d*9}" x2="${q.x-dx/d*10}" y2="${q.y-dy/d*10}"${mode==='direct'?' marker-end="url(#citationArrow)"':''}><title>${mode==='coupled'?l.shared+' références communes':'Citation directe'}</title></line>`;}).join('');
  const circles=m.nodes.map(item=>{const p=positions.get(item.key);return `<g role="button" tabindex="0" data-network-key="${esc(item.key)}" aria-label="${esc(item.data.title+', '+yearOf(item)+', explorer les liens')}" aria-pressed="${String(item.key===focus)}"><title>${esc(item.data.title)} (${esc(yearOf(item))})</title><circle cx="${p.x}" cy="${p.y}" r="${item.key===focus?9:6}" class="${item.key===focus?'selected-node':''}"/></g>`;}).join('');
  $('networkGraph').innerHTML=m.nodes.length?`<svg viewBox="0 0 900 560" aria-label="Réseau bibliographique interactif ; sélectionnez un document avec le clavier ou la liste" xmlns="http://www.w3.org/2000/svg"><defs><marker id="citationArrow" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="5" markerHeight="5" orient="auto-start-reverse"><path d="M0 0 L10 5 L0 10 Z"/></marker></defs><g class="network-edges">${lines}</g><g class="network-nodes">${circles}</g></svg>`:'<p class="empty">Aucun lien disponible pour ce document ou ce seuil. Essayez les références communes ou revenez à la vue d’ensemble.</p>';
  const selected=m.current.get(focus);
  function chooser(key,label){const item=m.current.get(key);return `<li><button type="button" data-network-key="${esc(key)}">${esc(item.data.title)}</button><small>${esc(yearOf(item)||'Sans date')}${label?' · '+esc(label):''}</small></li>`;}
  if(selected){
    const neighbors=m.fullLinks.filter(l=>l.source===focus||l.target===focus);
    $('networkDetails').innerHTML=`<h3>${titleLink(selected)}</h3><p>${esc(authorsOf(selected))} · ${esc(yearOf(selected))}</p><p><a href="${esc(canonicalUrl(selected))}" target="_blank" rel="noopener">Notice Zotero</a> · <a href="${esc(m.indexed.get(focus).openalex)}" target="_blank" rel="noopener">Source OpenAlex</a></p><h4>${neighbors.length} lien${neighbors.length>1?'s':''} bibliographique${neighbors.length>1?'s':''}</h4><ul>${neighbors.map(l=>chooser(l.source===focus?l.target:l.source,mode==='coupled'?l.shared+' références communes':l.source===focus?'cité par ce document':'cite ce document')).join('')}</ul>`;
  }else{
    const degree=new Map();for(const l of m.fullLinks)for(const key of [l.source,l.target])degree.set(key,(degree.get(key)||0)+1);
    const top=[...degree].sort((a,b)=>b[1]-a[1]||a[0].localeCompare(b[0])).slice(0,15);
    $('networkDetails').innerHTML='<h3>Explorer un document</h3><p>Sélectionnez un point ou un titre. Ces documents ont le plus de liens dans ce réseau ; ce n’est pas un classement d’impact.</p><ul>'+top.map(([key,count])=>chooser(key,count+' liens')).join('')+'</ul>';
  }
  const missing=m.documents.filter(i=>!m.connected.has(i.key));
  $('networkMissing').innerHTML=`<p>${missing.length} documents sans lien dans ce mode et à ce seuil.</p><ul>${missing.map(i=>`<li>${titleLink(i)} · ${esc(yearOf(i)||'Sans date')} <small>(${!m.indexed.has(i.key)?'non retrouvé par DOI':!m.indexed.get(i.key).referenceCount?'bibliographie non indexée':'aucun lien au sein du corpus'})</small> · <a href="${esc(canonicalUrl(i))}" target="_blank" rel="noopener">Zotero</a></li>`).join('')}</ul>`;
}
for(const id of ['networkMode','networkThreshold','networkFocus'])document.getElementById(id).addEventListener('change',renderPublicationNetwork);
document.getElementById('networkReset').addEventListener('click',()=>{$('networkFocus').value='';renderPublicationNetwork();});
function selectNetworkNode(event){const node=event.target.closest('[data-network-key]');if(!node)return;if(event.type==='keydown'&&!['Enter',' '].includes(event.key))return;if(event.type==='keydown')event.preventDefault();$('networkFocus').value=node.dataset.networkKey;renderPublicationNetwork();$('networkFocus').focus();}
document.getElementById('networkGraph').addEventListener('click',selectNetworkNode);
document.getElementById('networkGraph').addEventListener('keydown',selectNetworkNode);
document.getElementById('networkDetails').addEventListener('click',selectNetworkNode);
