from __future__ import annotations
import argparse
from nila import __version__

def main() -> int:
    parser=argparse.ArgumentParser(prog="nila",description="Nila LocalAI")
    parser.add_argument("--version",action="version",version=f"%(prog)s {__version__}")
    sub=parser.add_subparsers(dest="command")
    sub.add_parser("doctor",help="Check local runtime and privacy prerequisites")
    sub.add_parser("setup",help="Run local-first setup")
    args=parser.parse_args()
    if args.command=="doctor":
        print("Nila LocalAI doctor: secure foundation installed; runtime checks pending.")
        return 0
    if args.command=="setup":
        print("Nila LocalAI setup: secure foundation installed; automation pending.")
        return 0
    parser.print_help(); return 0

if __name__=="__main__": raise SystemExit(main())
