from __future__ import annotations
from dataclasses import dataclass

@dataclass(frozen=True)
class TeacherProvider:
    name:str
    api_base:str
    key_name:str
    protocol:str="openai-compatible"

PROVIDERS={
 "openai":TeacherProvider("openai","https://api.openai.com/v1","OPENAI_API_KEY"),
 "gemini":TeacherProvider("gemini","https://generativelanguage.googleapis.com","GEMINI_API_KEY","gemini"),
 "anthropic":TeacherProvider("anthropic","https://api.anthropic.com","ANTHROPIC_API_KEY","anthropic"),
 "openrouter":TeacherProvider("openrouter","https://openrouter.ai/api/v1","OPENROUTER_API_KEY"),
 "ollama-cloud":TeacherProvider("ollama-cloud","https://ollama.com/api","OLLAMA_API_KEY","ollama"),
}
def get_provider(name:str)->TeacherProvider:
    try:return PROVIDERS[name.strip().lower()]
    except KeyError as e:raise ValueError(f"NLA-1801: unsupported teacher provider: {name}") from e
