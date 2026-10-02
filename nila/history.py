from __future__ import annotations
import json,sqlite3,uuid
from datetime import datetime,timezone
from pathlib import Path
class ChatStore:
 def __init__(self,path:Path):
  path.parent.mkdir(parents=True,exist_ok=True);self.path=path
  with sqlite3.connect(path) as d:d.execute("CREATE TABLE IF NOT EXISTS chats(id TEXT PRIMARY KEY,title TEXT NOT NULL,messages TEXT NOT NULL,updated_at TEXT NOT NULL)")
 def create(self,title="New chat"):
  i=uuid.uuid4().hex;self.save(i,title,[]);return i
 def save(self,i,title,messages):
  stamp=datetime.now(timezone.utc).isoformat()
  with sqlite3.connect(self.path) as d:d.execute("INSERT OR REPLACE INTO chats VALUES(?,?,?,?)",(i,title,json.dumps(messages,ensure_ascii=False),stamp))
 def get(self,i):
  with sqlite3.connect(self.path) as d:r=d.execute("SELECT id,title,messages,updated_at FROM chats WHERE id=?",(i,)).fetchone()
  return None if not r else {"id":r[0],"title":r[1],"messages":json.loads(r[2]),"updated_at":r[3]}
 def list(self):
  with sqlite3.connect(self.path) as d:r=d.execute("SELECT id,title,updated_at FROM chats ORDER BY updated_at DESC").fetchall()
  return [{"id":x[0],"title":x[1],"updated_at":x[2]} for x in r]
 def delete(self,i):
  with sqlite3.connect(self.path) as d:d.execute("DELETE FROM chats WHERE id=?",(i,))
