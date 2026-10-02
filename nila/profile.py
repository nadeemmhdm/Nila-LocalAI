from __future__ import annotations
import json, os, secrets
from dataclasses import asdict,dataclass
from pathlib import Path

@dataclass(frozen=True)
class Profile:
    assistant_name:str="Nila"
    owner_address:str="User"
    wake_phrase:str="Hey Nila"
    languages:tuple[str,...]=("ml","en")
    response_style:str="Malayalam/Manglish"

def save(profile:Profile,data_dir:Path)->Path:
    data_dir.mkdir(parents=True,exist_ok=True)
    target=data_dir/"profile.json"; tmp=target.with_suffix(".tmp-"+secrets.token_hex(4))
    payload=asdict(profile); payload["languages"]=list(profile.languages)
    with open(tmp,"w",encoding="utf-8") as f:
        json.dump(payload,f,indent=2,ensure_ascii=False); f.flush(); os.fsync(f.fileno())
    if os.name!="nt": os.chmod(tmp,0o600)
    os.replace(tmp,target); return target
