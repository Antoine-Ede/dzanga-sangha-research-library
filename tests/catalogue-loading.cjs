const fs=require('node:fs'),vm=require('node:vm'),assert=require('node:assert/strict');
const source=fs.readFileSync(require('node:path').join(__dirname,'../app.js'),'utf8');
const code=source.slice(source.indexOf('async function fetchAll'),source.indexOf('function tagsOf'));
async function run(){
  let active=0,peak=0;
  const mocked=async url=>{
    const start=Number(new URL(url).searchParams.get('start'));
    active++;peak=Math.max(peak,active);
    await new Promise(resolve=>setTimeout(resolve,2));active--;
    return {ok:true,headers:new Headers({'Total-Results':'501','Last-Modified-Version':'42'}),
      json:async()=>Array.from({length:Math.min(100,501-start)},(_,n)=>({key:start+n}))};
  };
  const context=vm.createContext({fetch:mocked,AbortSignal});
  vm.runInContext(code,context);
  const items=await context.fetchAll('https://example.org/items');
  assert.equal(items.length,501);assert.equal(new Set(items.map(i=>i.key)).size,501);
  assert.equal(peak,3);assert.equal(items[500].key,500);
  context.fetch=async url=>{const r=await mocked(url);if(new URL(url).searchParams.get('start')!=='0')r.headers.set('Last-Modified-Version','43');return r;};
  await assert.rejects(()=>context.fetchAll('https://example.org/items'),/catalogue a changé/);
  console.log('PASS pagination: complete, ordered, maximum three requests; concurrent changes rejected.');
  if(process.argv.includes('--live')){
    const endpoint='https://api.zotero.org/groups/6701789/items/top?format=json';
    let start=performance.now(),serial=[];
    for(let offset=0;;offset+=100){
      const r=await fetch(endpoint+'&limit=100&start='+offset);
      if(!r.ok)throw new Error('Public API '+r.status);
      const page=await r.json();serial.push(...page);if(page.length<100)break;
    }
    const serialMs=Math.round(performance.now()-start);
    context.fetch=fetch;start=performance.now();
    const parallel=await context.fetchAll(endpoint);
    const parallelMs=Math.round(performance.now()-start);
    assert.deepEqual(Array.from(parallel,i=>i.key).sort(),serial.map(i=>i.key).sort());
    console.log(JSON.stringify({checkedAt:new Date().toISOString(),items:parallel.length,serialMs,parallelMs,note:'Single ordered comparison; server and cache variability. No secret or writes.'}));
  }
}
run().catch(error=>{console.error(error.message);process.exitCode=1;});
