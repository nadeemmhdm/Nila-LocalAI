from __future__ import annotations
import json,urllib.request,urllib.parse
from nila.providers import get_provider
from nila.secrets import get_api_key
def _request(url,body,headers):
 req=urllib.request.Request(url,json.dumps(body).encode(),{"Content-Type":"application/json",**headers})
 with urllib.request.urlopen(req,timeout=120) as r:return json.load(r)
def ask(provider,model,prompt):
 p=get_provider(provider);key=get_api_key(provider)
 if not key:raise RuntimeError(f"NLA-1802: API key missing for {provider}")
 if p.protocol=="openai-compatible":
  d=_request(p.api_base+"/chat/completions",{"model":model,"messages":[{"role":"user","content":prompt}]},{"Authorization":"Bearer "+key})
  return d["choices"][0]["message"]["content"]
 if p.protocol=="anthropic":
  d=_request(p.api_base+"/v1/messages",{"model":model,"max_tokens":4096,"messages":[{"role":"user","content":prompt}]},{"x-api-key":key,"anthropic-version":"2023-06-01"})
  return "".join(x.get("text","") for x in d["content"])
 if p.protocol=="gemini":
  url=p.api_base+"/v1beta/models/"+urllib.parse.quote(model,safe="")+":generateContent?key="+urllib.parse.quote(key,safe="")
  d=_request(url,{"contents":[{"parts":[{"text":prompt}]}]},{});return d["candidates"][0]["content"]["parts"][0]["text"]
 if p.protocol=="ollama":
  d=_request(p.api_base+"/chat",{"model":model,"messages":[{"role":"user","content":prompt}],"stream":False},{"Authorization":"Bearer "+key})
  return d["message"]["content"]
 raise RuntimeError("NLA-1801: unsupported provider protocol")
