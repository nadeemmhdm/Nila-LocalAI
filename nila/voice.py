from __future__ import annotations
import shutil,subprocess
from pathlib import Path
def capabilities():
 return {"whisper":bool(shutil.which("whisper-cli") or shutil.which("whisper")),"piper":bool(shutil.which("piper"))}
def transcribe(audio:Path,model:Path)->str:
 exe=shutil.which("whisper-cli") or shutil.which("whisper")
 if not exe:raise RuntimeError("NLA-1201: local STT unavailable")
 r=subprocess.run([exe,"-m",str(model),"-f",str(audio),"-nt"],capture_output=True,text=True,timeout=300)
 if r.returncode:raise RuntimeError("NLA-1201: "+r.stderr[-500:])
 return r.stdout.strip()
def speak(text:str,model:Path,out:Path)->Path:
 exe=shutil.which("piper")
 if not exe:raise RuntimeError("NLA-1202: local TTS unavailable")
 r=subprocess.run([exe,"--model",str(model),"--output_file",str(out)],input=text,text=True,capture_output=True,timeout=300)
 if r.returncode:raise RuntimeError("NLA-1202: "+r.stderr[-500:])
 return out
