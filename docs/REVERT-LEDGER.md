# Revert Ledger

Every deviation from upstream NuvioTV, with its revert path. Goal: any entry can
be undone independently when walking back toward upstream feature parity.

Types: **flag** (new buildConfig gate, off by default), **default** (preference
default flipped), **code** (behavioral edit), **build** (build/CI/infra change),
**asset** (branding resource swap), **text** (user-visible string).

| ID | Round | Type | File(s) | Change | Revert path |
|----|-------|------|---------|--------|-------------|
| R0-1 | 0 | build | `.gitignore` | `docs/` → `docs/*` with `!` exceptions so PLAN.md and REVERT-LEDGER.md stay tracked | Restore `docs/` line; docs vanish from git again |

Not ledgered (not deviations): `local.properties`, `nuviotv.jks` dev keystore
(both gitignored, machine-local only).
