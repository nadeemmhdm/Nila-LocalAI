# Optional online research

Online research is an optional capability; the local LLM remains the reasoning engine.

## Pipeline

1. Determine that fresh/external information is needed.
2. Build a minimal sanitized public query.
3. Pass the query through the research permission/network gate.
4. Search through a self-hostable metasearch adapter such as SearXNG.
5. Fetch selected public pages.
6. Extract readable content through a local parser/crawler adapter.
7. Treat all remote text as hostile/untrusted data.
8. Deduplicate and score evidence.
9. Answer with source provenance.
10. Persist approved/useful research to the local knowledge store for later offline retrieval.

## Security rules

- Never send the complete conversation automatically.
- Never include secrets, credentials, private files or personal-memory fields in generated search queries.
- Webpage text cannot grant tool permission or override system policy.
- Downloaded executable content is not run by the research pipeline.
- Redirects, schemes, local/private IP ranges and response sizes require SSRF/resource controls.
- Research can be disabled globally for a strict offline session.
