# Revert Ledger

Every deviation from upstream NuvioTV, with its revert path. Goal: any entry can
be undone independently when walking back toward upstream feature parity.

Types: **flag** (new buildConfig gate, off by default), **default** (preference
default flipped), **code** (behavioral edit), **build** (build/CI/infra change),
**asset** (branding resource swap), **text** (user-visible string).

| ID | Round | Type | File(s) | Change | Revert path |
|----|-------|------|---------|--------|-------------|
| R0-1 | 0 | build | `.gitignore` | `docs/` → `docs/*` with `!` exceptions so PLAN.md and REVERT-LEDGER.md stay tracked | Restore `docs/` line; docs vanish from git again |
| R1-1 | 1 | build | `app/build.gradle.kts` | applicationIds: `com.nuvio.tv`→`app.pordal.tv`, `com.nuvio.app`→`app.pordal.tv.store`, debug overrides →`app.pordal.tv.dev`/`app.pordal.tv.store.dev` | Permanent identity — never revert (would collide with NuvioTV installs) |
| R1-2 | 1 | build | `app/build.gradle.kts` | `GITHUB_OWNER`/`GITHUB_REPO` → `pordal-app`/`PordalTV` | Permanent — upstream values would "update" users back to NuvioTV |
| R1-3 | 1 | build | `app/build.gradle.kts` | full flavor `FEATURE_IN_APP_UPDATES_ENABLED` → `false` | Set back to `true` in Round 6 once a Pordal release exists |
| R1-4 | 1 | build | `app/build.gradle.kts` | version → `0.2.0-beta` / 1035 | Permanent; release script bumps from here |
| R1-5 | 1 | build | `app/build.gradle.kts` | removed hardcoded `815787` keystore password fallbacks | Keep — signing now fails loudly instead of silently using upstream's dev passwords |
| R1-6 | 1 | text | `values/strings.xml`, `debug/res/values/strings.xml` | `app_name` → Pordal / Pordal Debug | Permanent identity |
| R1-7 | 1 | code | `NetworkModule.kt`, `SupportersContributorsScreen.kt` | blank `DONATIONS_BASE_URL`/`DONATIONS_DONATE_URL` fall back to `https://placeholder.invalid` instead of crashing DI (`error()`) | Restore `error()` calls if a donations backend is ever configured; candidate to upstream |

Not ledgered (not deviations): `local.properties`, `nuviotv.jks` dev keystore
(both gitignored, machine-local only).
