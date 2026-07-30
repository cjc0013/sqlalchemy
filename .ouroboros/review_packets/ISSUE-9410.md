# Issue review unit â€” document dataclass gotchas so far

- **Covered issues:** #9410
- **Review unit:** `COMMIT-168923e135fc82b0b5a01b2b91a69725c7b7ecf5`
- **Shape:** standalone-commit
- **Apply once:** not shared
- **Frozen base:** `aa1a5575358d3aa14953b04dced02f4763fed2e7`
- **Suggested target:** Maintainer choice; this unit has no changelog fragment
- **Subsystem:** documentation

## Problem and intended behavior

- **Issue #9410:** document dataclass gotchas so far

## Scope and provenance

- Issue #9410: `verified_local_option_closure`

Changed files:

- `doc/build/orm/dataclasses.rst`

Overlapping review units: none identified

## Validation

No separate focused receipt is borrowed for this issue unit. Changed test files
are listed below, and the complete publication-tree validation is reported
without turning it into an issue-specific claim.

Changed test files:

No issue-specific test file is isolated.

- Non-typing suite: 25800 passed, 1502 skipped, 0 failed, 0 errors.
- Typing suite: 77 passed; its recorded failure boundary matches the frozen upstream baseline.

Changelog files:

No issue-specific changelog file is isolated.

## Apply

```bash
git cherry-pick 168923e135fc82b0b5a01b2b91a69725c7b7ecf5
```

Inspect:

```bash
git show --stat 168923e135fc82b0b5a01b2b91a69725c7b7ecf5
git show 168923e135fc82b0b5a01b2b91a69725c7b7ecf5
```

## Consumption note

Use the command only for this listed technical unit; blank commands are deliberate evidence boundaries.
