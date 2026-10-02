from __future__ import annotations
from dataclasses import dataclass
from enum import Enum
from nila.privacy import sanitize_research_query

class TeacherPurpose(str,Enum):
    KNOWLEDGE="knowledge"
    DATASET="dataset"
    EVALUATION="evaluation"

@dataclass(frozen=True)
class TeacherRequest:
    provider:str
    model:str
    prompt:str
    purpose:TeacherPurpose

def prepare_request(provider:str,model:str,prompt:str,purpose:TeacherPurpose,*,secrets:tuple[str,...]=())->TeacherRequest:
    """Prepare an explicit cloud-teacher request without private context."""
    clean=sanitize_research_query(prompt,secrets=secrets)
    return TeacherRequest(provider=provider.strip().lower(),model=model.strip(),prompt=clean,purpose=purpose)

def cloud_training_enabled()->bool:
    """Cloud teachers are opt-in and never part of normal local inference."""
    import os
    return os.getenv("NILA_TEACHER_ENABLED","0").strip()=="1"
