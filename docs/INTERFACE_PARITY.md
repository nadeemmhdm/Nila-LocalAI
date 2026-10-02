# Web UI and CLI Feature Parity

Nila LocalAI has two first-class interfaces: Web UI and CLI.

## Contract

Business logic must live in reusable core services. The Web UI and CLI are clients of those same services; neither interface owns a private implementation of a product capability.

A user-facing capability is considered complete only when it is accessible from both interfaces, except capabilities that are inherently visual or inherently terminal-oriented. Even then, an equivalent operation/status must be exposed where technically meaningful.

## Required parity

Both interfaces must support:

- local AI chat and conversation management;
- setup, Doctor and repair;
- model discovery, download, install, select, start, stop and remove;
- voice/STT/TTS/wake model management and settings;
- assistant identity, languages, response style and privacy settings;
- memory search, inspect, export and delete;
- local knowledge search, inspect, ingest, refresh and delete;
- teacher-provider configuration and API-key management;
- topic learning, dataset generation and evaluation jobs;
- online research controls and research history;
- files, terminal, computer tools and permission policies;
- agents, routines, missions and execution history;
- updates, release information and diagnostics.

## Core-service rule

```text
                    +----------------+
Web UI ------------>|                |
                    | Nila Core/API  |---- Local LLM
CLI ---------------->|                |---- Memory/Knowledge
                    +----------------+---- Voice
                              |       ---- Tools/Agents
                              +------------ Research/Teachers
```

The local service binds to loopback by default. Web and CLI authorization, validation, privacy gates, permissions, audit events and error codes are enforced in the core rather than duplicated in clients.

## API keys

Keys are written to and read from the OS credential store through the core secret service. Web UI and CLI may add/test/remove a key, but neither should display the complete stored secret after saving it.

## Definition of done

Every feature pull request must identify:
1. core service/API;
2. CLI command;
3. Web UI surface;
4. permission/privacy behavior;
5. tests for core behavior and interface parity.

A feature missing one required interface remains incomplete.
