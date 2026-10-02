from pathlib import Path
from nila.models import installed
def test_installed_ignores_partial(tmp_path):
 (tmp_path/"a.gguf").write_bytes(b"x");(tmp_path/"b.part").write_bytes(b"x")
 assert installed(tmp_path)==["a.gguf"]
