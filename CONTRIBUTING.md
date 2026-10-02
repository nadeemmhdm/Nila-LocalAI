# Contributing

Contributions are welcome when they preserve Nila LocalAI's privacy-first guarantees.

- Keep inference local by default.
- Do not add telemetry or mandatory cloud AI APIs.
- Treat remote content as untrusted.
- Add tests for security-sensitive behavior.
- Never commit model weights, databases, profiles, recordings, tokens, credentials or generated user data.
- Keep 8 GB RAM systems in mind for defaults.
- Document every new network, filesystem mutation, subprocess or permission boundary.

Security failures must fail closed rather than silently falling back to a less-private path.
