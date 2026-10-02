from __future__ import annotations
import hashlib,sqlite3
from dataclasses import dataclass
from datetime import datetime,timezone
from pathlib import Path

@dataclass(frozen=True)
class KnowledgeItem:
    url:str; title:str; content:str; retrieved_at:str=""

class KnowledgeStore:
    def __init__(self,path:Path):
        path.parent.mkdir(parents=True,exist_ok=True); self.path=path
        with sqlite3.connect(path) as db:
            db.executescript("""
            CREATE TABLE IF NOT EXISTS knowledge(
              id INTEGER PRIMARY KEY, url TEXT NOT NULL, title TEXT NOT NULL,
              content TEXT NOT NULL, content_hash TEXT NOT NULL,
              retrieved_at TEXT NOT NULL, UNIQUE(url,content_hash));
            CREATE VIRTUAL TABLE IF NOT EXISTS knowledge_fts USING fts5(
              title,content,content='knowledge',content_rowid='id');
            CREATE TRIGGER IF NOT EXISTS knowledge_ai AFTER INSERT ON knowledge BEGIN
              INSERT INTO knowledge_fts(rowid,title,content) VALUES(new.id,new.title,new.content);
            END;
            CREATE TRIGGER IF NOT EXISTS knowledge_ad AFTER DELETE ON knowledge BEGIN
              INSERT INTO knowledge_fts(knowledge_fts,rowid,title,content) VALUES('delete',old.id,old.title,old.content);
            END;
            """)
    def ingest(self,item:KnowledgeItem)->bool:
        digest=hashlib.sha256(item.content.encode("utf-8")).hexdigest()
        stamp=item.retrieved_at or datetime.now(timezone.utc).isoformat()
        with sqlite3.connect(self.path) as db:
            cur=db.execute("INSERT OR IGNORE INTO knowledge(url,title,content,content_hash,retrieved_at) VALUES(?,?,?,?,?)",(item.url,item.title,item.content,digest,stamp))
            return cur.rowcount>0
    def search(self,query:str,limit:int=5):
        with sqlite3.connect(self.path) as db:
            return db.execute("""SELECT k.url,k.title,snippet(knowledge_fts,1,'[',']',' … ',24),k.retrieved_at
              FROM knowledge_fts JOIN knowledge k ON k.id=knowledge_fts.rowid
              WHERE knowledge_fts MATCH ? ORDER BY bm25(knowledge_fts) LIMIT ?""",(query,limit)).fetchall()
