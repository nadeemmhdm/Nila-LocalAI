from __future__ import annotations
import ipaddress
from urllib.parse import urlparse

class PrivacyViolation(RuntimeError): pass

def is_loopback_url(url:str)->bool:
    p=urlparse(url if "://" in url else "http://"+url)
    host=(p.hostname or "").lower().rstrip(".")
    if host=="localhost": return True
    try: return ipaddress.ip_address(host).is_loopback
    except ValueError: return False

def require_local_inference(url:str)->None:
    if not is_loopback_url(url):
        raise PrivacyViolation("NLA-1301: inference endpoint must be loopback")

def sanitize_research_query(query:str, *, secrets:tuple[str,...]=())->str:
    clean=" ".join(query.replace("\n"," ").split()).strip()
    for secret in secrets:
        if secret: clean=clean.replace(secret,"[redacted]")
    if not clean: raise PrivacyViolation("NLA-1302: empty research query after sanitization")
    return clean[:500]
