import pytest
from nila.tools import safe_read,safe_write,ToolDenied
def test_file_guard(tmp_path):
 safe_write(tmp_path,"a/b.txt","ok");assert safe_read(tmp_path,"a/b.txt")=="ok"
 with pytest.raises(ToolDenied):safe_read(tmp_path,"../outside")
