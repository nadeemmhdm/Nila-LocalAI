from __future__ import annotations
SERVICE="nila-localai"
def set_api_key(provider:str,value:str)->None:
    if not value.strip(): raise ValueError("API key cannot be empty")
    import keyring
    keyring.set_password(SERVICE,provider.strip().lower(),value.strip())
def get_api_key(provider:str)->str|None:
    import keyring
    return keyring.get_password(SERVICE,provider.strip().lower())
def delete_api_key(provider:str)->None:
    import keyring
    try:keyring.delete_password(SERVICE,provider.strip().lower())
    except keyring.errors.PasswordDeleteError:pass
