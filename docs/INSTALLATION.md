# Installation

Nila LocalAI is designed around a one-command installer, but the automated installer is not considered production-ready until its dependency, checksum, rollback and platform tests pass.

## Target platforms

- Windows 11 x64 first-class target
- Linux x86_64
- macOS Apple Silicon / Intel where dependencies are available
- 8 GB RAM minimum target for the conservative local profile

## Automated setup contract

The installer must:

1. detect OS and architecture;
2. verify RAM and free disk;
3. install/locate Python and required runtime components;
4. install a pinned llama.cpp build;
5. download a compatible GGUF model with integrity metadata;
6. install local speech/wake components;
7. create private runtime/data directories;
8. run Doctor;
9. configure user-approved OS autostart;
10. start the local UI.

Re-running the installer must be idempotent and act as repair/update rather than destroying user data.

## Model downloads

Hugging Face credentials, when required, are download credentials only. They must never be attached to inference, memory, telemetry, research, or voice traffic.
