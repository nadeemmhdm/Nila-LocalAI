from __future__ import annotations
import json,urllib.request
from dataclasses import dataclass
from nila.privacy import require_local_inference
@dataclass(frozen=True)
class ChatResult: content:str; model:str
def chat(messages:list[dict],base_url:str="http://127.0.0.1:8080",model:str="local")->ChatResult:
    require_local_inference(base_url)
    body=json.dumps({"model":model,"messages":messages,"stream":False}).encode()
    req=urllib.request.Request(base_url.rstrip("/")+"/v1/chat/completions",body,{"Content-Type":"application/json"})
    try:
        with urllib.request.urlopen(req,timeout=120) as r:data=json.load(r)
    except Exception as e: raise RuntimeError(f"NLA-1102: local inference failed: {e}") from e
    return ChatResult(data["choices"][0]["message"]["content"],data.get("model",model))
