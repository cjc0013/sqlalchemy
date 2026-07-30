# Issue review unit â€” synonym descriptors automatically blend existing properties - undocumented?

- **Covered issues:** #4706
- **Review unit:** `COMMIT-278cf421a6b18c01ef463e9b97b9cd245082e9de`
- **Shape:** standalone-commit
- **Apply once:** not shared
- **Frozen base:** `aa1a5575358d3aa14953b04dced02f4763fed2e7`
- **Suggested target:** Maintainer choice; this unit has no changelog fragment
- **Subsystem:** ORM

## Problem and intended behavior

- **Issue #4706:** synonym descriptors automatically blend existing properties - undocumented?

## Scope and provenance

- Issue #4706: `verified_local_option_closure`

Changed files:

- `lib/sqlalchemy/orm/_orm_constructors.py`

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
git cherry-pick 278cf421a6b18c01ef463e9b97b9cd245082e9de
```

Inspect:

```bash
git show --stat 278cf421a6b18c01ef463e9b97b9cd245082e9de
git show 278cf421a6b18c01ef463e9b97b9cd245082e9de
```

## Consumption note

Use the command only for this listed technical unit; blank commands are deliberate evidence boundaries.
