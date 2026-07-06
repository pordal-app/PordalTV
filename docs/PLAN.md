# Pordal Rebuild — Plan & Status

Rebuild of the Pordal PoC on a fresh fork of NuvioTV (upstream 0.7.16-beta /
versionCode 1034), following `REBUILD-PLAYBOOK.md` from the first (scattershot)
build. One round = one coherent commit, verified on the emulator before moving on.

**Strategy (non-negotiable):** ship a lean PoC, walk back toward upstream feature
parity later. Gate features behind flags or flip defaults — never delete code.
Keep internals aligned with upstream (`com.nuvio.tv` package, `Nuvio*` classes,
resource IDs, persistence keys, `NUVIO_RELEASE_*` secret names) to preserve
`git merge upstream/dev` viability.

Every deviation from upstream is recorded in [REVERT-LEDGER.md](REVERT-LEDGER.md).

## Rounds

| # | Theme | Status |
|---|---|---|
| 0 | Env setup + docs scaffolding | done (56802dc1) |
| 1 | Identity + backend detach (app IDs, name, GitHub owner/repo, versioning, keystore fallbacks, donations no-op patch) | in progress |
| 2 | Feature gates + default flips (accounts, pickers, settings, cloud tab; catalog suffix/addon-name, autoplay, overlays) | pending |
| 3 | Default addons + boot-gate emission bug fix (if still present upstream) | pending |
| 4 | Visual assets (icons, banners, logos, splash `#051D2A`) — blocked on brand masters location | pending |
| 5 | Text sweep (strings.xml ×33, Kotlin literals, README/workflows/templates) | pending |
| 6 | Release infra (release_beta.py fix, CI secrets re-add, R8 validation, first release) | pending |

## Fixed facts

- Addon: `http://addon.pordal.app:60201` (catalog/meta/stream, movie+series, IMDb
  `tt…` IDs, no subtitles resource — keep OpenSubtitles).
- App IDs: `app.pordal.tv` (full) / `app.pordal.tv.store` (playstore) / `.dev`
  suffix for debug (NOT `.debug` — benchmark buildType owns it). Everything under
  `app.pordal.tv.*` so future non-TV Pordal apps get their own namespace.
- GitHub: `pordal-app/PordalTV`; releases wiped by the re-fork (old 0.1.0-beta /
  versionCode 2 is gone). CI secrets must be re-added before Round 6.
- Splash: `#051D2A`.

## Open decisions

- Location of brand-asset masters (Figma export folder moved from `~/Downloads`).

Resolved: versioning restarts at `0.2.0-beta` / versionCode 1035 (above upstream's
1034 and the old released Pordal versionCode 2).

## Verification protocol (after each round)

Emulator `Television_4K`, `adb install -r` the arm64 fullDebug APK:
1. Fresh-install boot → straight to Home (no sign-in, no pickers) — from Round 2 on.
2. Home rows populate from `addon.pordal.app` (logcat `CatalogRepository`) — Round 3+.
3. Sidebar: Home/Search/Library only; Library: no Cloud tab, no LOCAL badge — Round 2+.
4. Title → detail → play → straight into playback (no source list) — Round 2+.
5. Google TV Apps row shows the Pordal banner tile — Round 4+.
6. `grep -ri nuvio` over `res/values*/strings.xml` → no user-visible hits — Round 5+.
