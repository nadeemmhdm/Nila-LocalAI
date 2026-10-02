from __future__ import annotations
import os
from nila.chat import chat
from nila.history import ChatStore
from nila.knowledge import KnowledgeStore
from nila.paths import data_dir
class NilaService:
 def __init__(self):
  d=data_dir();self.chats=ChatStore(d/"chats.db");self.knowledge=KnowledgeStore(d/"brain.db")
 def send(self,text,chat_id=None):
  cid=chat_id or self.chats.create(text[:60] or "New chat");row=self.chats.get(cid);msgs=row["messages"]
  context=self.knowledge.search(text,3)
  if context: msgs.append({"role":"system","content":"Relevant local knowledge:\n"+"\n".join(x[2] for x in context)})
  msgs.append({"role":"user","content":text})
  out=chat(msgs,os.getenv("NILA_LLM_URL","http://127.0.0.1:8080"),os.getenv("NILA_MODEL","local"))
  msgs.append({"role":"assistant","content":out.content});self.chats.save(cid,row["title"],msgs)
  return {"chat_id":cid,"content":out.content,"model":out.model}
