# Architecture

Nila LocalAI separates private local intelligence from optional external research.

## Local plane
Owns identity, preferences, conversation memory, knowledge retrieval, LLM inference, voice, agents, tools and audit history. It must remain functional without internet after installation.

## Research plane
Disabled in offline mode. When explicitly enabled it receives a sanitized query, not the full conversation/memory state. Search and crawl results are hostile input.

Ingestion records source URL, title, retrieval time, content hash and freshness metadata before local indexing.

## Memory layers
1. Working context
2. Searchable conversation recall
3. Explicit editable user profile
4. Local knowledge store
5. Bounded agent/routine state

Web-derived knowledge remains distinguishable from user facts and assistant summaries.

## Runtime
The conservative profile uses llama.cpp on 127.0.0.1 and a Qwen3 1.7B-class GGUF Q4_K_M target for 8 GB systems.

## Tool security
Read-only and mutating capabilities are separate. Terminal, writes, computer control, downloads and destructive operations use explicit policy gates and auditable outcomes.
