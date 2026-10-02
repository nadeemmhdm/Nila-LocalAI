import pytest
from nila.privacy import PrivacyViolation,require_local_inference,sanitize_research_query
def test_local_inference_only():
    require_local_inference("http://127.0.0.1:8080")
    with pytest.raises(PrivacyViolation): require_local_inference("https://example.com/v1")
def test_research_redacts_known_secret():
    q=sanitize_research_query("weather token-123 Kerala",secrets=("token-123",))
    assert "token-123" not in q and "[redacted]" in q
