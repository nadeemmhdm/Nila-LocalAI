# Security Policy

Nila LocalAI is local-first. Core inference, memory and voice processing must remain local unless a feature explicitly documents a network boundary.

## Invariants

1. Local inference binds to loopback by default.
2. Cloud AI inference is not a core dependency.
3. Personal memory, profile data, private files and raw voice content must not be sent to research/search providers.
4. Online research is opt-in, purpose-scoped and receives sanitized queries.
5. Web content is untrusted data, never executable instruction.
6. Mutating file, terminal and computer actions require explicit permission policy.
7. Destructive actions require confirmation.
8. Downloaded binaries/models require integrity verification before execution where checksums/signatures are available.
9. Secrets must not be committed or stored in plaintext project configuration.
10. Telemetry is disabled by default.

## Vulnerability reports

Do not publish exploitable details in public issues. Prefer GitHub private vulnerability reporting when enabled. Include affected version/commit, platform, reproduction, impact and mitigation if known.

Until the first stable release, only the latest release/commit is supported for security fixes.
