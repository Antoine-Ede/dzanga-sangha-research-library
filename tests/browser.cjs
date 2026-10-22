// Real headless browser; fictitious Zotero responses and no external traffic.
const fs=require('node:fs');
const path=require('node:path');
const os=require('node:os');
const http=require('node:http');
const assert=require('node:assert/strict');
const {createRequire}=require('node:module');
const root=path.resolve(__dirname,'..');
function playwright(){
  try{return require('playwright');}catch(error){
    if(error.code!=='MODULE_NOT_FOUND')throw error;
    const bundled=path.join(os.homedir(),'.cache/codex-runtimes/codex-primary-runtime/dependencies/node/node_modules/playwright/package.json');
    if(!fs.existsSync(bundled))throw new Error('Playwright required: install locally or use an existing Codex runtime. No automatic download.');
    return createRequire(bundled)('playwright');
  }
}
async function main(){
  const allowed=new Set(['index.html','app.js','library-model.js','analytics.js','quality.js','styles.css','assets/ds-logo-transp-schwarz.png']);
  const fixtures=JSON.parse(fs.readFileSync(path.join(__dirname,'fixtures/browser-items.json'),'utf8'));
  const server=http.createServer((req,res)=>{
    const name=new URL(req.url,'http://localhost').pathname.slice(1)||'index.html';
    if(!allowed.has(name)){res.writeHead(404).end();return;}
    const type=name.endsWith('.js')?'text/javascript':name.endsWith('.css')?'text/css':name.endsWith('.png')?'image/png':'text/html';
    res.writeHead(200,{'Content-Type':type});res.end(fs.readFileSync(path.join(root,name)));
  });
  await new Promise(resolve=>server.listen(0,'127.0.0.1',resolve));
  let browser;
  try{
    const {chromium}=playwright();
    // Prefer an installed browser on Windows, otherwise Playwright's installed binary.
    const chrome=path.join(process.env.PROGRAMFILES||'', 'Google/Chrome/Application/chrome.exe');
    browser=await chromium.launch({headless:true,...(process.platform==='win32'&&fs.existsSync(chrome)?{executablePath:chrome}:{})});
    const context=await browser.newContext({viewport:{width:1440,height:1000},serviceWorkers:'block'});
    const origin=`http://127.0.0.1:${server.address().port}`;
    const errors=[],blocked=[];
    await context.route('**/*',async route=>{
      const request=route.request(),url=new URL(request.url());
      if(url.origin===origin)return route.continue();
      // Navigation contract only; the real public PDF is checked separately.
      if(request.url()==='https://example.org/public-copy.pdf')return route.fulfill({contentType:'text/html',body:'<p>Synthetic PDF destination</p>'});
      if(request.url()==='https://example.org/synthetic')return route.fulfill({contentType:'text/html',body:'<p>Synthetic repository record, no full text</p>'});
      if(url.origin==='https://api.zotero.org'&&request.method()==='GET'){
        const isItems=url.pathname==='/groups/6701789/items/top';
        const isCollections=url.pathname==='/groups/6701789/collections';
        if(isItems||isCollections)return route.fulfill({json:isItems?fixtures:[]});
      }
      blocked.push(url.origin);return route.abort();
    });
    const page=await context.newPage();page.on('pageerror',error=>errors.push(error.message));
    page.on('dialog',async dialog=>{errors.push('Unexpected dialog');await dialog.dismiss();});
    await page.goto(origin);await page.waitForLoadState('networkidle');
    await page.locator('#libraryTab:enabled').waitFor();
    assert.match(await page.locator('#resultCount').innerText(),/3 résultats sur 3/);
    const out=path.join(root,'.local/browser');fs.mkdirSync(out,{recursive:true});
    for(const view of ['cards','list','table']){
      await page.locator('#resultView').selectOption(view);
      const pdf=page.locator('#results a.document-pdf');
      assert.equal(await pdf.count(),1);
      assert.equal(await pdf.getAttribute('href'),'https://example.org/public-copy.pdf');
      assert.equal(await page.getByRole('link',{name:'Notice Zotero',exact:true}).count(),3);
      const source=page.locator('#results a.document-source');
      assert.equal(await source.count(),1);
      assert.equal(await source.getAttribute('href'),'https://example.org/synthetic');
      assert.equal(await source.innerText(),'Source en ligne');
      assert.equal(await page.getByRole('link',{name:'Article synthétique — auteurs à vérifier',exact:true}).getAttribute('href'),'https://example.org/synthetic');
      await source.focus();
      const sourceOpened=page.waitForEvent('popup');await page.keyboard.press('Enter');
      const sourceDestination=await sourceOpened;await sourceDestination.waitForLoadState();
      assert.equal(await sourceDestination.locator('p').innerText(),'Synthetic repository record, no full text');
      await sourceDestination.close();
      const pdfTitle=page.getByRole('link',{name:'Rapport synthétique — archive de démonstration',exact:true});
      assert.equal(await pdfTitle.getAttribute('href'),'https://example.org/public-copy.pdf');
      await pdfTitle.focus();
      const opened=page.waitForEvent('popup');await page.keyboard.press('Enter');
      const destination=await opened;await destination.waitForLoadState();
      assert.equal(destination.url(),'https://example.org/public-copy.pdf');
      assert.equal(await destination.locator('p').innerText(),'Synthetic PDF destination');
      await destination.close();
      const archive=page.locator('#results .archive-info').filter({hasText:'APDS-DEMO'});
      const summary=archive.locator('summary');
      assert.equal(await archive.locator('details').getAttribute('open'),null);
      let visible=await archive.innerText();
      assert(!visible.includes('Access verification'));
      assert(visible.includes('À préciser :'));
      assert(visible.includes('Original sensible : consultation encadrée aux APDS.'));
      assert.equal((visible.match(/APDS-DEMO/g)||[]).length,1);
      await summary.focus();await page.keyboard.press('Enter');
      await page.locator('#results details[open]').waitFor();
      assert((await archive.innerText()).includes('Réserve spécifique : annexe absente.'));
      assert.equal(await archive.locator('img,script').count(),0);
      await page.keyboard.press('Enter');
      assert.equal(await archive.locator('details').getAttribute('open'),null);
      await page.locator('#results').screenshot({path:path.join(out,`${view}.png`)});
    }
    // Author values are preserved: suspicious data is signalled, not silently rewritten.
    await page.locator('#authorFilter').selectOption('a');
    assert.match(await page.locator('#resultCount').innerText(),/1 résultat sur 3/);
    assert((await page.locator('#results').innerText()).includes('auteurs à vérifier'));
    await page.locator('#resetFilters').click();
    await page.locator('#search').fill('texte libre');
    assert.match(await page.locator('#resultCount').innerText(),/1 résultat sur 3/);
    await page.locator('#results summary').click();
    assert((await page.locator('#results').innerText()).includes('annexe non retrouvée'));
    await page.locator('#resetFilters').click();
    await page.locator('#analysisTab').click();
    assert(await page.locator('#analysisPanel').isVisible());
    assert((await page.locator('#analysisSummary').innerText()).includes('Documents'));
    await page.locator('#qualityTab').click();
    await page.locator('#qualityIssue').selectOption({label:'Nom/prénom à vérifier : nom réduit à des initiales (1)'});
    assert.match(await page.locator('#qualityCount').innerText(),/1 notices à examiner sur 3/);
    assert((await page.locator('#qualityResults').innerText()).includes('auteurs à vérifier'));
    await page.locator('#libraryTab').click();
    await page.locator('#search').fill('texte libre');
    await page.locator('#helpTab').focus();await page.keyboard.press('Enter');
    assert(await page.locator('#helpPanel').isVisible());
    for(const id of ['searchPanel','statsPanel','libraryPanel','analysisPanel','qualityPanel','exportCsv'])assert(await page.locator('#'+id).isHidden());
    assert.equal(await page.locator('#helpTab').getAttribute('aria-pressed'),'true');
    assert.equal(new URL(page.url()).searchParams.get('section'),'help');
    assert((await page.locator('#help-pdfs').innerText()).includes('Consulter le PDF'));
    await page.screenshot({path:path.join(out,'help-desktop.png'),fullPage:true});
    await page.setViewportSize({width:390,height:844});
    assert(await page.evaluate(()=>document.documentElement.scrollWidth<=innerWidth+2));
    await page.screenshot({path:path.join(out,'help-mobile.png'),fullPage:true});
    await page.locator('#libraryTab').click();
    assert.equal(await page.locator('#search').inputValue(),'texte libre');
    assert.match(await page.locator('#resultCount').innerText(),/1 résultat sur 3/);
    await page.locator('#resetFilters').click();
    await page.locator('#resultView').selectOption('list');
    await page.setViewportSize({width:390,height:844});
    await page.locator('#results').screenshot({path:path.join(out,'mobile-list.png')});
    assert(await page.evaluate(()=>document.documentElement.scrollWidth<=innerWidth+2));
    const downloadPromise=page.waitForEvent('download');await page.locator('#exportCsv').click();
    const download=await downloadPromise;await download.saveAs(path.join(out,'synthetic-export.csv'));
    assert(fs.readFileSync(path.join(out,'synthetic-export.csv'),'utf8').includes('Durand A'));
    // The guide deep link and navigation remain usable when public Zotero fails.
    await context.route('https://api.zotero.org/**',route=>route.fulfill({status:403,json:{error:'Synthetic denied'}}));
    const unavailable=await context.newPage();unavailable.on('pageerror',error=>errors.push(error.message));
    await unavailable.goto(origin+'/?section=help&q=preserved');await unavailable.waitForLoadState('networkidle');
    assert(await unavailable.locator('#helpPanel').isVisible());
    assert(await unavailable.locator('#helpTab').isEnabled());
    assert(await unavailable.locator('#searchPanel').isHidden());
    assert(await unavailable.locator('#exportCsv').isHidden());
    await unavailable.locator('#helpTab').click();
    assert.equal(new URL(unavailable.url()).searchParams.get('section'),'help');
    await unavailable.screenshot({path:path.join(out,'help-api-unavailable.png'),fullPage:true});
    await unavailable.close();
    assert.deepEqual(errors,[]);assert.deepEqual(blocked,[]);
    fs.writeFileSync(path.join(out,'result.json'),JSON.stringify({passed:true,browser:browser.version(),data:'synthetic only',views:['cards','list','table'],keyboard:true,mobile:true,help:true,helpDeepLink:true,helpWithApiFailure:true,externalTraffic:0,limits:['not a screen-reader audit','not scientific validation','user review pending']},null,2));
    console.log('PASS browser: three views, keyboard, filters, analysis, quality, mobile, CSV and guide with API failure; no external traffic');
  }finally{
    if(browser)await browser.close();
    await new Promise(resolve=>server.close(resolve));
  }
}
main().catch(error=>{console.error(error);process.exitCode=1;});
