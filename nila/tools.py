from __future__ import annotations
from pathlib import Path
class ToolDenied(RuntimeError):pass
def safe_read(root:Path,relative:str)->str:
 root=root.resolve();p=(root/relative).resolve()
 if p!=root and root not in p.parents:raise ToolDenied("NLA-1701: path outside allowed root")
 return p.read_text(encoding="utf-8")
def safe_write(root:Path,relative:str,content:str)->Path:
 root=root.resolve();p=(root/relative).resolve()
 if p!=root and root not in p.parents:raise ToolDenied("NLA-1701: path outside allowed root")
 p.parent.mkdir(parents=True,exist_ok=True);p.write_text(content,encoding="utf-8");return p
