# Memory and local knowledge

Nila separates personal memory from researched knowledge.

## Personal memory

Conversation recall, preferences, explicit profile facts and agent state stay local. Personal memory is never automatically copied into a web-search query.

## Knowledge memory

Online research can be retained for offline use. Each stored document/chunk carries provenance:

- canonical source URL;
- page title;
- retrieval timestamp;
- content hash;
- source type;
- freshness/expiry hint;
- trust/review state.

The system retrieves this knowledge locally when offline. Stored web content remains untrusted evidence, not an instruction to the agent.

## User controls

The product must provide inspect, search, export, forget/delete and refresh controls. Deleting a source must also remove derived chunks/index entries associated with it.
