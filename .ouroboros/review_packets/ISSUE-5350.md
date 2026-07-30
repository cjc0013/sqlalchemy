# Issue review unit â€” `NoReferencedColumnError` when using `referred_column_0[[_]N]_name` in FK naming convention

- **Covered issues:** #5350
- **Review unit:** `COMMIT-908451977266e19296ca8059bf42ce8d50a20f92`
- **Shape:** standalone-commit
- **Apply once:** not shared
- **Frozen base:** `aa1a5575358d3aa14953b04dced02f4763fed2e7`
- **Suggested target:** Maintainer choice; this unit has no changelog fragment
- **Subsystem:** SQL expression language

## Problem and intended behavior

- **Issue #5350:** `NoReferencedColumnError` when using `referred_column_0[[_]N]_name` in FK naming convention

## Scope and provenance

- Issue #5350: `verified_local_option_closure`

Changed files:

- `test/sql/test_metadata.py`

Overlapping review units: COMMIT-70e6b730b53852e27ec5699f6309eba92e820c8c

## Validation

No separate focused receipt is borrowed for this issue unit. Changed test files
are listed below, and the complete publication-tree validation is reported
without turning it into an issue-specific claim.

Changed test files:

- `test/sql/test_metadata.py`

- Non-typing suite: 25800 passed, 1502 skipped, 0 failed, 0 errors.
- Typing suite: 77 passed; its recorded failure boundary matches the frozen upstream baseline.

Changelog files:

No issue-specific changelog file is isolated.

## Apply

```bash
git cherry-pick 908451977266e19296ca8059bf42ce8d50a20f92
```

Inspect:

```bash
git show --stat 908451977266e19296ca8059bf42ce8d50a20f92
git show 908451977266e19296ca8059bf42ce8d50a20f92
```

## Consumption note

Use the command only for this listed technical unit; blank commands are deliberate evidence boundaries.
