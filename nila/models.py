from __future__ import annotations
import hashlib,urllib.request
from dataclasses import dataclass
from pathlib import Path
@dataclass(frozen=True)
class DownloadSpec: name:str;url:str;sha256:str|None=None
def download(spec:DownloadSpec,dest:Path)->Path:
 dest.mkdir(parents=True,exist_ok=True);target=dest/spec.name;part=target.with_suffix(target.suffix+".part")
 with urllib.request.urlopen(spec.url,timeout=60) as r,open(part,"wb") as f:
  while True:
   b=r.read(1024*1024)
   if not b:break
   f.write(b)
 if spec.sha256:
  h=hashlib.sha256(part.read_bytes()).hexdigest()
  if h.lower()!=spec.sha256.lower():part.unlink(missing_ok=True);raise RuntimeError("NLA-1602: download integrity failed")
 part.replace(target);return target
def installed(dest:Path):return sorted(x.name for x in dest.glob("*") if x.is_file() and not x.name.endswith(".part"))
