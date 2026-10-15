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
  assert(html.includes('Notice incomplète'));
  assert(html.includes('consultation encadrée aux APDS'));
  assert(html.includes('Manuscrit ou projet de recherche'));
  assert(html.includes(view==='table'?'Non renseignés':'Auteur non renseigné'));
}
assert.equal(archiveInfo({data:{}}),'');
assert.equal(safeUrl('javascript:alert(1)'),'');
assert.equal(LibraryModel.category({data:{itemType:'report'}}),'reports');
assert.equal(LibraryModel.category({data:{itemType:'dataset'}}),'datasets');
assert(!LibraryModel.issues(testItem).some(x=>/DOI/.test(x)));
console.log('PASS: synthetic rendering, escaping, missing metadata, controlled originals and categories');
`, context);
