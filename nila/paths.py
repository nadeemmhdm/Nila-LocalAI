from pathlib import Path
import os
def data_dir()->Path:
    root=os.getenv("NILA_DATA_DIR")
    return Path(root).expanduser() if root else Path.home()/".nila-localai"
