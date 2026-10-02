from nila.history import ChatStore
def test_chat_crud(tmp_path):
 s=ChatStore(tmp_path/"c.db");i=s.create("Hello");s.save(i,"Hello",[{"role":"user","content":"hi"}])
 assert s.get(i)["messages"][0]["content"]=="hi";assert s.list()[0]["id"]==i;s.delete(i);assert s.get(i) is None
