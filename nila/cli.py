from __future__ import annotations
import argparse,getpass
from nila import __version__
from nila.paths import data_dir
from nila.service import NilaService
from nila.providers import PROVIDERS
from nila.secrets import set_api_key,delete_api_key

def main()->int:
 p=argparse.ArgumentParser(prog="nila",description="Nila LocalAI")
 p.add_argument("--version",action="version",version=f"%(prog)s {__version__}")
 s=p.add_subparsers(dest="command")
 s.add_parser("chat",help="Interactive local chat")
 s.add_parser("chats",help="List conversations")
 serve=s.add_parser("serve",help="Start Web UI");serve.add_argument("--host",default="127.0.0.1");serve.add_argument("--port",type=int,default=47821)
 key=s.add_parser("teacher",help="Manage teacher providers");ks=key.add_subparsers(dest="teacher_command")
 ka=ks.add_parser("add");ka.add_argument("provider",choices=PROVIDERS.keys())
 kr=ks.add_parser("remove");kr.add_argument("provider",choices=PROVIDERS.keys())
 ks.add_parser("list")
 learn=s.add_parser("learn",help="Prepare a topic-learning job");learn.add_argument("topic")
 s.add_parser("brain",help="Search local knowledge").add_argument("query")
 s.add_parser("doctor");s.add_parser("setup")
 a=p.parse_args();svc=NilaService()
 if a.command=="serve":
  import uvicorn;uvicorn.run("nila.web:app",host=a.host,port=a.port,reload=False);return 0
 if a.command=="chat":
  cid=None
  print("Nila LocalAI. /new starts a new chat; /exit quits.")
  while True:
   try:q=input("You> ").strip()
   except (EOFError,KeyboardInterrupt):break
   if q in {"/exit","/quit"}:break
   if q=="/new":cid=None;continue
   if q:
    try:r=svc.send(q,cid);cid=r["chat_id"];print("Nila>",r["content"])
    except Exception as e:print(str(e))
  return 0
 if a.command=="chats":
  for x in svc.chats.list():print(x["id"],x["title"])
  return 0
 if a.command=="teacher":
  if a.teacher_command=="list":
   for n,v in PROVIDERS.items():print(n,v.protocol)
  elif a.teacher_command=="add":set_api_key(a.provider,getpass.getpass(f"{a.provider} API key: "));print("Saved to OS credential store.")
  elif a.teacher_command=="remove":delete_api_key(a.provider);print("Removed.")
  else:key.print_help()
  return 0
 if a.command=="brain":
  for x in svc.knowledge.search(a.query,10):print(f"{x[1]}\n{x[2]}\n{x[0]}\n")
  return 0
 if a.command=="learn":
  print("Topic learning provider execution is not implemented yet; no fake job was started.");return 2
 if a.command=="doctor":
  print("data:",data_dir());print("core: OK");print("runtime: verify llama.cpp separately");return 0
 if a.command=="setup":print("Setup automation is not implemented yet.");return 2
 p.print_help();return 0
if __name__=="__main__":raise SystemExit(main())
