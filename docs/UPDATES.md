# Updates

The planned updater follows published GitHub Releases.

## User experience

- Check for a newer release at application start when networking is enabled.
- Show a dismissible dashboard announcement for a new version.
- Provide an Update action in Settings/Dashboard.
- Provide a CLI update command.
- Do not repeatedly show a dismissed announcement for the same release.
- A newer release may display a new announcement.

## Security

Release artifacts must be integrity-checked before execution. A failed checksum/signature, interrupted staging transaction or incompatible platform must fail closed and preserve the working installation. User data directories are not replaced by application updates.

Automatic background installation must be configurable; security updates may be announced prominently but are not permitted to bypass integrity checks.
