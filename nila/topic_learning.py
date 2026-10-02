from __future__ import annotations
import hashlib
from dataclasses import dataclass
from datetime import datetime,timezone
from nila.knowledge import KnowledgeItem,KnowledgeStore
from nila.teacher import TeacherPurpose,prepare_request

@dataclass(frozen=True)
class Lesson:
    topic:str
    provider:str
    model:str
    content:str
    source_ref:str

def learning_prompt(topic:str)->str:
    return ("Create a factual study note about this public topic: "+topic+
      ". Cover definitions, important concepts, limitations, common misconceptions, "
      "and facts worth retaining. Clearly mark uncertainty. Do not invent citations.")

def prepare_topic(topic:str,provider:str,model:str):
    return prepare_request(provider,model,learning_prompt(topic),TeacherPurpose.KNOWLEDGE)

def save_lesson(store:KnowledgeStore,lesson:Lesson)->bool:
    digest=hashlib.sha256((lesson.provider+"\0"+lesson.model+"\0"+lesson.content).encode()).hexdigest()[:20]
    ref=lesson.source_ref or f"teacher://{lesson.provider}/{lesson.model}/{digest}"
    title=f"{lesson.topic} — teacher {lesson.provider}/{lesson.model}"
    return store.ingest(KnowledgeItem(ref,title,lesson.content,datetime.now(timezone.utc).isoformat()))
