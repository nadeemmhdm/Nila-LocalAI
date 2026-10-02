from __future__ import annotations
import json,urllib.request
RELEASES="https://api.github.com/repos/nadeemmhdm/Nila-LocalAI/releases/latest"
def latest():
 req=urllib.request.Request(RELEASES,headers={"Accept":"application/vnd.github+json","User-Agent":"Nila-LocalAI"})
 try:
  with urllib.request.urlopen(req,timeout=10) as r:d=json.load(r)
  return {"tag":d.get("tag_name"),"url":d.get("html_url")}
 except Exception as e:raise RuntimeError(f"NLA-1601: update check failed: {e}") from e
