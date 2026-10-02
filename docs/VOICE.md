# Local voice

Voice is designed to work without a cloud service.

Pipeline:

```text
Microphone -> local wake detector -> local STT -> local LLM -> local TTS -> speaker
```

The conservative target uses multilingual Whisper-class local STT, a lightweight local TTS engine/voice pack, and Vosk/openWakeWord-class wake detection.

Raw recordings are transient by default. Persisting recordings requires an explicit setting. Transcripts follow the same local memory/privacy policy as typed conversations.
