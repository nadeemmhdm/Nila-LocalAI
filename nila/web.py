from __future__ import annotations
from fastapi import FastAPI,HTTPException
from fastapi.responses import HTMLResponse
from pydantic import BaseModel
from nila.service import NilaService
from nila.providers import PROVIDERS
from nila.secrets import set_api_key,delete_api_key
app=FastAPI(title="Nila LocalAI",docs_url="/api/docs")
svc=NilaService()
class Msg(BaseModel): text:str; chat_id:str|None=None
class Key(BaseModel): key:str
@app.get("/api/health")
def health():return {"ok":True,"mode":"local"}
@app.get("/api/chats")
def chats():return svc.chats.list()
@app.get("/api/chats/{cid}")
def get_chat(cid:str):
 r=svc.chats.get(cid)
 if not r:raise HTTPException(404,"chat not found")
 return r
@app.delete("/api/chats/{cid}")
def del_chat(cid:str):svc.chats.delete(cid);return {"ok":True}
@app.post("/api/chat")
def send(m:Msg):return svc.send(m.text,m.chat_id)
@app.get("/api/providers")
def providers():return [{"name":x.name,"protocol":x.protocol} for x in PROVIDERS.values()]
@app.put("/api/providers/{name}/key")
def key(name:str,k:Key):
 if name not in PROVIDERS:raise HTTPException(404,"provider not found")
 set_api_key(name,k.key);return {"ok":True}
@app.delete("/api/providers/{name}/key")
def delkey(name:str):delete_api_key(name);return {"ok":True}
@app.get("/",response_class=HTMLResponse)
def ui():return HTML
HTML=r'''<!doctype html><html><head><meta charset="utf-8"><meta name="viewport" content="width=device-width"><title>Nila</title><style>
*{box-sizing:border-box}body{margin:0;font:15px system-ui;background:#0b0b0c;color:#eee}.app{display:grid;grid-template-columns:270px 1fr;height:100vh}.side{border-right:1px solid #252529;padding:14px;background:#111113}.brand{font-size:20px;font-weight:700;margin:8px}.new{width:100%;padding:12px;border:1px solid #333;border-radius:12px;background:#1a1a1e;color:#fff}.chats{margin-top:18px}.chat{padding:10px;border-radius:9px;cursor:pointer;white-space:nowrap;overflow:hidden}.chat:hover{background:#202024}.main{display:flex;flex-direction:column}.top{height:58px;border-bottom:1px solid #222;padding:18px 24px}.msgs{flex:1;overflow:auto;max-width:850px;width:100%;margin:auto;padding:30px}.m{padding:13px 16px;margin:12px 0;border-radius:16px;white-space:pre-wrap}.user{background:#242429;margin-left:18%}.assistant{margin-right:12%}.composer{max-width:850px;width:calc(100% - 30px);margin:12px auto 22px;display:flex;gap:8px;background:#19191d;border:1px solid #303036;padding:9px;border-radius:20px}textarea{flex:1;resize:none;background:none;border:0;color:#fff;outline:0;padding:8px;font:inherit}button{cursor:pointer}.send{border:0;border-radius:14px;padding:0 18px}.empty{text-align:center;margin-top:20vh;font-size:28px;font-weight:650}@media(max-width:700px){.app{grid-template-columns:1fr}.side{display:none}.msgs{padding:18px}.user{margin-left:8%}}
</style></head><body><div class="app"><aside class="side"><div class="brand">Nila</div><button class="new" onclick="newChat()">+ New chat</button><div id="chats" class="chats"></div></aside><main class="main"><div class="top">Nila LocalAI · Local</div><div id="msgs" class="msgs"><div class="empty">How can I help you?</div></div><div class="composer"><textarea id="q" rows="1" placeholder="Message Nila..."></textarea><button class="send" onclick="send()">↑</button></div></main></div><script>
let cid=null;const E=id=>document.getElementById(id);
async function load(){let a=await(await fetch('/api/chats')).json();E('chats').innerHTML=a.map(x=>'<div class="chat" onclick="openChat(\''+x.id+'\')">'+esc(x.title)+'</div>').join('')}
function esc(s){return String(s).replace(/[&<>"]/g,c=>({'&':'&amp;','<':'&lt;','>':'&gt;','"':'&quot;'}[c]))}
function draw(ms){E('msgs').innerHTML=ms.length?ms.filter(x=>x.role!='system').map(x=>'<div class="m '+x.role+'">'+esc(x.content)+'</div>').join(''):'<div class="empty">How can I help you?</div>';E('msgs').scrollTop=E('msgs').scrollHeight}
async function openChat(id){cid=id;let r=await(await fetch('/api/chats/'+id)).json();draw(r.messages)}
function newChat(){cid=null;draw([])}
async function send(){let q=E('q').value.trim();if(!q)return;E('q').value='';let current=cid?await(await fetch('/api/chats/'+cid)).json():{messages:[]};draw([...current.messages,{role:'user',content:q},{role:'assistant',content:'Thinking…'}]);let r=await fetch('/api/chat',{method:'POST',headers:{'Content-Type':'application/json'},body:JSON.stringify({text:q,chat_id:cid})});let j=await r.json();if(!r.ok){draw([...current.messages,{role:'user',content:q},{role:'assistant',content:j.detail||'Error'}]);return}cid=j.chat_id;await openChat(cid);load()}
E('q').addEventListener('keydown',e=>{if(e.key==='Enter'&&!e.shiftKey){e.preventDefault();send()}});load()
</script></body></html>'''
