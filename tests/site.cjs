// Ported from the existing private verify_archive_ui.cjs; only fictitious metadata.
const fs = require('node:fs');
const vm = require('node:vm');
const assert = require('node:assert/strict');
const path = require('node:path');
const root = path.resolve(__dirname, '..');
const src = fs.readFileSync(path.join(root, 'app.js'), 'utf8');
const boundary = src.indexOf('["search",...Object.keys(FILTERS)');
assert(boundary > 0);
const nodes = new Map();
const document = {getElementById(id){if(!nodes.has(id)) nodes.set(id,{value:'',checked:false,innerHTML:'',textContent:''}); return nodes.get(id);}};
const LibraryModel = require('../library-model.js');
const context = vm.createContext({document, URL, console, assert, LibraryModel});
vm.runInContext(src.slice(0,boundary), context);
vm.runInContext(`
const testItem={key:'SYNTHETIC',data:{title:'Synthetic archive',itemType:'manuscript',creators:[],date:'',archive:'Bibliothèque <img src=x onerror=alert(1)>',archiveLocation:'APDS-SYNTHETIC',extra:'Copie conservée dans la Bibliothèque des APDS.\\nInformations manquantes : auteur, date.\\nOriginal contenant des éléments sensibles <script>alert(1)</script>',tags:[{tag:'STATUS:Metadata-Incomplete'},{tag:'ACCESS:Restricted-Original'}],collections:[]}};
state.items=[testItem];state.filtered=[testItem];
for(const view of ['table','cards','list']) {
  $('resultView').value=view;render();const html=$('results').innerHTML;
  assert(!html.includes('<img'));assert(!html.includes('<script>'));
  assert(html.includes('&lt;img'));assert(html.includes('&lt;script&gt;'));
  assert(html.includes('À préciser :'));
  assert(html.includes('Détails de la notice Zotero'));
  assert(html.includes('consultation encadrée aux APDS'));
  assert(html.includes('Manuscrit ou projet de recherche'));
  assert(html.includes(view==='table'?'Non renseignés':'Auteur non renseigné'));
}
assert.equal(archiveInfo({data:{}}),'');
assert.equal(safeUrl('javascript:alert(1)'),'');
for (const url of ['', 'https://example.org/article', 'javascript:alert(1)', 'https://user:pass@example.org/file.pdf', 'https://example.org/file.pdf/page']) {
  assert.equal(pdfUrl({data:{url}}),'');
}
const pdfItem={...testItem,data:{...testItem.data,url:'https://example.org/copy.PDF?download=1&label=%22',DOI:'10.1234/example'}};
const unchanged=JSON.stringify(pdfItem);
assert(pdfUrl(pdfItem));
assert.equal(articleUrl(pdfItem),pdfUrl(pdfItem));
assert.equal(articleUrl({data:{DOI:'10.1234/example',url:'https://hal.science/synthetic-record'}}),'https://doi.org/10.1234%2Fexample');
assert.equal(articleUrl({data:{DOI:'10.1234/example',url:'https://example.org/official-article'}}),'https://example.org/official-article');
assert.equal(articleUrl({data:{DOI:'10.1234/example',url:'https://example.org/pdf-download?id=1'}}),'https://example.org/pdf-download?id=1');
assert.equal(articleUrl({data:{DOI:'10.1234/example',url:'https://user:pass@example.org/article'}}),'https://doi.org/10.1234%2Fexample');
assert.equal(articleUrl({data:{url:'https://example.org/official-article'}}),'https://example.org/official-article');
state.items=[pdfItem];state.filtered=[pdfItem];
for(const view of ['table','cards','list']) {
  $('resultView').value=view;render();const html=$('results').innerHTML;
  assert.equal((html.match(/Consulter le PDF/g)||[]).length,1);
  assert(html.includes('Notice Zotero'));
  assert(html.includes('consultation encadrée aux APDS'));
  assert(html.includes('&amp;label='));
  assert(titleLink(pdfItem).includes('https://example.org/copy.PDF?download=1&amp;label=%22'));
}
assert.equal(JSON.stringify(pdfItem),unchanged);
const repositoryItem={...testItem,data:{...testItem.data,url:'https://hal.science/synthetic-record',DOI:'10.1234/synthetic'}};
state.items=[repositoryItem];state.filtered=[repositoryItem];
for(const view of ['table','cards','list']) {
  $('resultView').value=view;render();const html=$('results').innerHTML;
  assert.equal((html.match(/Notice HAL/g)||[]).length,1);
  assert(html.includes('https://hal.science/synthetic-record'));
  assert(html.includes('https://doi.org/10.1234%2Fsynthetic'));
  assert(!html.includes('Consulter le PDF'));
  assert(html.includes('Notice Zotero'));
}
for(const url of ['', 'javascript:alert(1)', 'https://user:pass@example.org/record', 'https://doi.org/10.1234/synthetic'])assert.equal(sourceLink({data:{url}}),'');
assert.equal(LibraryModel.category({data:{itemType:'report'}}),'reports');
assert.equal(LibraryModel.category({data:{itemType:'dataset'}}),'datasets');
assert(!LibraryModel.issues(testItem).some(x=>/DOI/.test(x)));
assert.equal(LibraryModel.authorNeedsReview({creatorType:'author',firstName:'Martin',lastName:'A'}),true);
for(const c of [{firstName:'A',lastName:'Martin'},{firstName:'Wei',lastName:'Li'},
  {name:'Institut ABC',firstName:'Martin',lastName:'A'},{firstName:'Martin',lastName:'A',creatorType:'translator'}]){
  assert.equal(LibraryModel.authorNeedsReview({creatorType:'author',...c}),false);
}
const retained={data:{creators:[{creatorType:'author',firstName:'Martin',lastName:'A'}],extra:'Texte libre sans marqueur APDS',tags:[]}};
const saved=JSON.stringify(retained);
assert(LibraryModel.issues(retained).includes('Nom/prénom à vérifier : nom réduit à des initiales'));
assert.equal(JSON.stringify(retained),saved);
assert.equal(LibraryModel.archiveSummary(retained).details,'Texte libre sans marqueur APDS');
assert.equal(LibraryModel.archiveSummary(retained).publicCopy,false);
const oneLine={data:{extra:'Informations manquantes ou à confirmer : auteur, date. Original contenant des éléments sensibles ; consultation encadrée.',tags:[]}};
assert.equal(JSON.stringify(LibraryModel.archiveSummary(oneLine).gaps),JSON.stringify(['auteur, date.']));
assert.equal(LibraryModel.archiveSummary(oneLine).sensitive,true);
console.log('PASS: synthetic rendering, escaping, missing metadata, controlled originals and categories');
`, context);
