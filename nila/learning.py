from __future__ import annotations
from dataclasses import dataclass
from nila.teacher_client import ask
from nila.topic_learning import Lesson,prepare_topic,save_lesson
from nila.knowledge import KnowledgeStore
@dataclass(frozen=True)
class LearningResult: topic:str;provider:str;model:str;saved:bool;content:str
def learn(store:KnowledgeStore,topic,provider,model):
 req=prepare_topic(topic,provider,model);content=ask(provider,model,req.prompt)
 if not content.strip():raise RuntimeError("NLA-1803: teacher returned empty lesson")
 saved=save_lesson(store,Lesson(topic,provider,model,content,""))
 return LearningResult(topic,provider,model,saved,content)
