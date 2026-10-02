from __future__ import annotations
from dataclasses import dataclass
@dataclass(frozen=True)
class Agent:
 name:str;instructions:str;model:str="local"
class AgentRegistry:
 def __init__(self):self._items={}
 def add(self,a:Agent):self._items[a.name]=a
 def get(self,name):return self._items.get(name)
 def list(self):return list(self._items.values())
