import pytest
from nila.chat import chat
def test_chat_blocks_remote_endpoint():
 with pytest.raises(Exception):chat([],"https://example.com")
