# Error codes

| Code | Area | Meaning |
|---|---|---|
| NLA-1001 | Setup | Required runtime is missing |
| NLA-1002 | Setup | Insufficient RAM or disk for selected profile |
| NLA-1101 | Model | Local GGUF model missing/invalid |
| NLA-1102 | Model | llama.cpp failed to start |
| NLA-1201 | Voice | Local STT unavailable |
| NLA-1202 | Voice | Local TTS unavailable |
| NLA-1203 | Voice | Wake/microphone unavailable |
| NLA-1301 | Privacy | Non-loopback inference endpoint blocked |
| NLA-1302 | Privacy | Research query rejected by privacy gate |
| NLA-1303 | Privacy | Network operation is not purpose-authorized |
| NLA-1401 | Research | Search provider unavailable |
| NLA-1402 | Research | Remote content rejected by fetch policy |
| NLA-1501 | Knowledge | Local knowledge database unavailable |
| NLA-1601 | Update | Release check failed |
| NLA-1602 | Update | Release integrity verification failed |
| NLA-1701 | Tool | Tool permission denied |
| NLA-1702 | Tool | Destructive action requires confirmation |

Security/privacy/integrity failures must fail closed. Do not silently downgrade or bypass them.
