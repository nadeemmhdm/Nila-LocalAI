# Nila LocalAI

**Privacy-first, offline-first personal AI for your own computer.**

Nila LocalAI is an open-source personal AI platform designed to keep the assistant, conversations, memory, voice processing and automation on the user's machine. Core operation does not require a cloud AI provider. When online research is explicitly enabled, Nila can gather public information, preserve source metadata, ingest useful knowledge locally and later retrieve it while offline.

## Core goals

- Local LLM inference through llama.cpp on loopback only
- 8 GB RAM-friendly default profile
- Local long-term memory, profile and knowledge base
- Local STT, TTS and wake word
- Files, terminal, computer tools, agents and routines with permission gates
- Optional source-aware online research isolated from private memory\n- Opt-in Topic Learning with OpenAI, Gemini, Anthropic, OpenRouter, Ollama Cloud and compatible teacher APIs\n- Teacher knowledge persisted locally for later offline retrieval
- First-run assistant/owner/wake/language/voice customization
- One-command setup, doctor, repair and verified updates
- No telemetry by default

## Default AI profile

Initial target: **Qwen3 1.7B GGUF Q4_K_M + llama.cpp**. Model weights are downloaded separately and are never committed here.

## Privacy boundary

Offline mode blocks external access. Connected research is opt-in and receives only sanitized research queries. Personal profile fields, private memories, private files and raw voice recordings are not valid research payloads. Remote content is untrusted and is stored with provenance before retrieval.

## Architecture

```text
Chat / Voice
    |
Identity + Local Memory + Knowledge
    |
Local LLM — llama.cpp @ 127.0.0.1
    |
Planner + Permission Gate
    |-- Files / Terminal / Computer
    |-- Agents / Routines
    |-- Offline Knowledge Retrieval
    |
Optional Research Gate
    |
Search / Fetch / Crawl
    |
Untrusted-content pipeline
    |
Provenance-aware local knowledge
```

## Status

Early secure foundation. Privacy/security invariants are implemented before autonomous capabilities are enabled.

## Documentation

| Guide | Purpose |
| --- | --- |
| [Architecture](docs/ARCHITECTURE.md) | System boundaries, memory layers and runtime design |
| [Installation](docs/INSTALLATION.md) | Supported platforms and automated setup contract |
| [Privacy](docs/PRIVACY.md) | Offline and connected-mode privacy guarantees |
| [Memory & Local Knowledge](docs/MEMORY.md) | Personal memory and persistent researched knowledge |
| [Online Research](docs/ONLINE_RESEARCH.md) | Safe optional web research pipeline |\n| Teacher APIs | Optional cloud-assisted topic learning; runtime inference stays local |
| [Local Voice](docs/VOICE.md) | Offline STT, TTS and wake-word design |
| [Updates](docs/UPDATES.md) | Verified release-update design |
| [Roadmap](docs/ROADMAP.md) | Implementation phases |
| [Error Codes](docs/ERROR_CODES.md) | Stable NLA error identifiers |
| [Security](SECURITY.md) | Security policy and reporting |
| [Contributing](CONTRIBUTING.md) | Contribution workflow |
| [Code of Conduct](CODE_OF_CONDUCT.md) | Community standards |

## License

Apache-2.0 for project source. Third-party models/components retain their own licenses. See [LICENSE](LICENSE) and [THIRD_PARTY.md](THIRD_PARTY.md).
