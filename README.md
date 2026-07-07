<div align="center">

  <img src="assets/brand/app_logo_mark.png" alt="Pordal" width="120" />

  # PordalTV

  <p>
    A lean Android TV media player powered by the Stremio addon ecosystem.
    <br />
    Kotlin • Jetpack Compose • TV-first playback
  </p>

</div>

## About

PordalTV is a streamlined media player for Android TV. It boots straight into a
curated home screen, resolves content and sources through Stremio-compatible
addons, and plays with a click — no accounts, no onboarding, no source-picking
ceremony.

PordalTV is a fork of the open-source
[NuvioTV](https://github.com/NuvioMedia/NuvioTV) project. Enormous credit to the
NuvioTV authors and contributors — the player engine, addon client, and UI
foundations are theirs. This fork trims the experience down to a
proof-of-concept shape (features are gated, not removed) and rebrands the
surface.

## Installation

Sideload the APK for your device architecture from
[Releases](https://github.com/pordal-app/PordalTV/releases) (arm64-v8a for
virtually all modern TV devices). Release builds check GitHub for updates and
prompt in-app.

## Building

JDK 17 and the Android SDK (platform 36) are required. Create
`local.properties` at the repo root with at least:

```properties
sdk.dir=/path/to/Android/sdk
TMDB_API_KEY=your_tmdb_v3_api_key
NUVIO_SUPABASE_URL=https://placeholder.invalid
NUVIO_SUPABASE_ANON_KEY=placeholder
NUVIO_RELEASE_KEY_ALIAS=nuviotv
NUVIO_RELEASE_KEY_PASSWORD=your_keystore_password
NUVIO_RELEASE_STORE_PASSWORD=your_keystore_password
```

All builds (including debug) sign with the release config: generate a
throwaway keystore at the repo root with
`keytool -genkeypair -keystore nuviotv.jks -alias nuviotv`. Then:

```sh
./gradlew :app:assembleFullDebug
```

Project documentation lives in [docs/PLAN.md](docs/PLAN.md); every deviation
from upstream is tracked in [docs/REVERT-LEDGER.md](docs/REVERT-LEDGER.md).

## License

Licensed under the [GNU General Public License v3.0](LICENSE), as inherited
from NuvioTV. Source code for this fork is maintained at
[pordal-app/PordalTV](https://github.com/pordal-app/PordalTV).

Metadata and artwork are provided by [TMDB](https://www.themoviedb.org/). This
product uses the TMDB API but is not endorsed or certified by TMDB.
