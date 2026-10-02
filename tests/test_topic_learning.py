from nila.knowledge import KnowledgeStore
from nila.topic_learning import Lesson,prepare_topic,save_lesson
def test_topic_request_is_knowledge_only():
    r=prepare_topic("Kerala geography","ollama-cloud","teacher-model")
    assert r.purpose.value=="knowledge" and "Kerala geography" in r.prompt
def test_lesson_saved_for_offline_search(tmp_path):
    s=KnowledgeStore(tmp_path/"brain.db")
    assert save_lesson(s,Lesson("Python","openai","teacher","Python is a programming language.",""))
    assert s.search("programming language")
