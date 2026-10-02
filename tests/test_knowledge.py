from nila.knowledge import KnowledgeItem,KnowledgeStore
def test_research_survives_for_offline_retrieval(tmp_path):
    s=KnowledgeStore(tmp_path/"brain.db")
    assert s.ingest(KnowledgeItem("https://example.test","Local AI","Nila stores researched knowledge locally"))
    assert not s.ingest(KnowledgeItem("https://example.test","Local AI","Nila stores researched knowledge locally"))
    rows=s.search("researched knowledge")
    assert rows and rows[0][0]=="https://example.test"
