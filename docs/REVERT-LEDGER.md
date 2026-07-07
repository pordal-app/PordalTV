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
| R2-1 | 2 | flag | `app/build.gradle.kts`, `MainActivity.kt`, `SettingsScreen.kt` | `FEATURE_ACCOUNTS_ENABLED=false`: skips first-boot QR sign-in, hides Settings→Account | Flip flag to `true` (needs Supabase backend, see PLAN roadmap) |
| R2-2 | 2 | flag | `app/build.gradle.kts`, `MainActivity.kt` | `FEATURE_ONBOARDING_PICKERS_ENABLED=false`: start destination forced Home, experience mode defaults ADVANCED | Flip flag to `true` |
| R2-3 | 2 | flag | `app/build.gradle.kts`, `MainActivity.kt` | `FEATURE_SETTINGS_MENU_ENABLED=false`: Settings removed from sidebar drawer | Flip flag to `true` |
| R2-4 | 2 | flag | `app/build.gradle.kts`, `LibraryScreen.kt` | `FEATURE_CLOUD_LIBRARY_TAB_ENABLED=false`: Cloud view-mode button hidden in Library | Flip flag to `true` |
| R2-5 | 2 | default | `LayoutPreferenceDataStore.kt` + UI-state initials (`HomeUiState`, `SearchUiState`, `FolderDetailViewModel`, `LayoutSettingsViewModel`, `HomeViewModelPresentationPipeline`) | `catalogAddonNameEnabled` and `catalogTypeSuffixEnabled` default `false` | Restore `?: true` / `= true` defaults |
| R2-6 | 2 | default | `PlayerSettingsDataStore.kt` | `streamAutoPlayMode` defaults `FIRST_STREAM` (read fallbacks only; UI transients stay MANUAL) | Restore `MANUAL` fallbacks |
| R2-7 | 2 | default | `PlayerSettingsDataStore.kt` | `loadingOverlayEnabled`, `showPlayerLoadingStatus` default `false` | Restore `true` defaults |
| R2-8 | 2 | default | `PlayerSettingsDataStore.kt` | preferred subtitle language defaults `"none"` (captions off at playback start; forced-subs migration path keeps `"en"`) | Restore `"en"` in data class + no-stored-value read fallback |
| R2-9 | 2 | default | `StreamBadgeSettings.kt`, `StreamBadgeSettingsDataStore.kt` | `showAddonLogo` defaults `false` (hides addon logo+name on stream cards, incl. player source panel) | Restore `true` defaults |
| R2-10 | 2 | code | `SearchDiscoverSection.kt` | catalog dropdown only rendered when >1 catalog; addon-name metadata segment honors `catalogAddonNameEnabled` | Remove `size > 1` gate / unconditionally `add(catalog.addonName)` |
| R2-11 | 2 | code | `LibraryScreen.kt` | source badge: `else` branch blank instead of "LOCAL"; `"NUVIO"` literal → `"PORDAL"` | Restore `library_source_local` string and `"NUVIO"` |
| R3-1 | 3 | default | `AddonPreferences.kt` | default addons: Cinemeta → `http://addon.pordal.app:60201` (OpenSubtitles kept — addon has no subtitles resource) | Restore `https://v3-cinemeta.strem.io`; only affects fresh installs (DataStore keeps existing users' addons) |
| R3-2 | 3 | code | `AddonRepositoryImpl.kt` | `getInstalledAddons()`: emit empty list when cold cache + failed manifest fetch (was: no emission → permanent black screen at boot gate) | Genuine upstream bug fix — keep; candidate to upstream |
| R3-3 | 3 | code | `PlayerScreen.kt`, `PostPlayOverlay.kt`, `values/strings.xml` | player pause overlay "via <stream>" hidden (`showVia = false`); next-episode countdown uses new `next_episode_playing_countdown` ("Playing in %1$ds") instead of "Playing via %1$s in %2$ds" | Restore `showVia` expression `!uiState.isPlaying && !uiState.currentStreamName.isNullOrBlank()` and the `next_episode_playing_via` branch (string + sourceName condition kept in tree) |
| R3-4 | 3 | code | `NuvioNavHost.kt` | playback-error back navigation lands on the Detail page (pop to existing detail entry, or navigate to one) instead of the source-selection screen; upstream stream-screen fallback kept for unknown contentId | Delete the Pordal branch at the top of `onPlaybackErrorBack`; the original body is intact below it |
| R4-1 | 4 | asset | 14 PNGs (5 mipmap launchers, drawable launcher/mark/wordmark/text/banners, xhdpi banner, `assets/brand/*`); deleted `assets/nuviotv.png` | Pordal art in every upstream filename, all at upstream's exact pixel sizes. `app_logo_wordmark.png` is the mark+text lockup (1085×344, Figma export). Masters: Jacob's Figma / `~/Downloads/Pordal TV Icons.zip` | Restore upstream PNGs from git history |
| R4-2 | 4 | text | `AddonWebPage.kt`, `DebridFormatterWebPage.kt`, `RepositoryWebPage.kt` | logo `alt="NuvioTV"` → `alt="Pordal"` (StreamBadgeWebPage already used app name) | Trivial string restore |
| R5-1 | 5 | text | all 33 `res/values*/strings.xml` | case-preserving Nuvio→Pordal sweep of string VALUES; resource IDs (`name="…"`) verified byte-identical; `licenses_attributions_nuvio_*` protected in every locale (GPL credit stays "Nuvio TV"), default-locale body gains "PordalTV is a fork of the open-source NuvioTV project." | Re-run sweep with inverted pairs, or restore files from upstream and re-apply |
| R5-2 | 5 | text | `NetworkModule.kt`, `SupabaseModule.kt`, `DebridSettingsViewModel.kt`, `CollectionManagement{Screen,ViewModel}.kt`, `AddonWebPage.kt`, `AuthQrSignInScreen.kt`, `AboutScreen.kt` | User-Agents → `Pordal/…`/`PordalTV/…`; TorBox device-auth name → "Pordal"; dead placeholder base URL → `placeholder.pordal.app`; collections export file → `pordal-collections.json` (4 spots); terms → `pordal.app/terms`, privacy → `pordal.app/privacy` | Restore literals from upstream; note terms/privacy pages must exist before public distribution (see PLAN roadmap) |
| R5-3 | 5 | build | `.github/workflows/*` (8), `.github/ISSUE_TEMPLATE/config.yml`, `PULL_REQUEST_TEMPLATE.md`, `CONTRIBUTING.md`, `README.md`, `scripts/release_beta.py`, `settings.gradle.kts`, `local.example.properties`; deleted stray `NuvioStreaming.code-workspace` | workflows swept lowercase-only (`NUVIO_RELEASE_*` secrets/props intact); issue-template links → pordal-app repo; README rewritten with upstream credit + GPL; release-notes normalizer → `pordal`; `rootProject.name` "My Application"→"PordalTV"; upstream telemetry example URL blanked | Per-file restore from upstream; README/CONTRIBUTING are full rewrites |

Not ledgered (not deviations): `local.properties`, `nuviotv.jks` dev keystore
(both gitignored, machine-local only).
