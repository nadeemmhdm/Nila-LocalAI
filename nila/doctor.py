from __future__ import annotations
import shutil,sys
from nila.paths import data_dir
from nila.voice import capabilities
def report():
 v=capabilities()
 return {"python":sys.version.split()[0],"data_dir":str(data_dir()),"llama_server":bool(shutil.which("llama-server")),"stt":v["whisper"],"tts":v["piper"]}
