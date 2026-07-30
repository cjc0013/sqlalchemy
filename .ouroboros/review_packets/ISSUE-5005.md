# Issue review unit â€” alter ORM-level "returned rows" checks to only warn if driver returns -1 or None

- **Covered issues:** #5005
- **Review unit:** `COMMIT-cb16d59854e4fa8bcbbeeed6f4938996c1763481`
- **Shape:** standalone-commit
- **Apply once:** not shared
- **Frozen base:** `aa1a5575358d3aa14953b04dced02f4763fed2e7`
- **Suggested target:** SQLAlchemy 2.1
- **Subsystem:** ORM

## Problem and intended behavior

- **Issue #5005:** alter ORM-level "returned rows" checks to only warn if driver returns -1 or None

## Scope and provenance

- Issue #5005: `verified_local_option_closure`

Changed files:

- `doc/build/changelog/unreleased_21/5005.rst`
- `lib/sqlalchemy/orm/dependency.py`
- `lib/sqlalchemy/orm/persistence.py`
- `test/orm/test_unitofworkv2.py`

Overlapping review units: COMMIT-019dfdaddee18c126a416ae920debc966400e68b

## Validation

No separate focused receipt is borrowed for this issue unit. Changed test files
are listed below, and the complete publication-tree validation is reported
without turning it into an issue-specific claim.

Changed test files:

- `test/orm/test_unitofworkv2.py`

- Non-typing suite: 25800 passed, 1502 skipped, 0 failed, 0 errors.
- Typing suite: 77 passed; its recorded failure boundary matches the frozen upstream baseline.

Changelog files:

- `doc/build/changelog/unreleased_21/5005.rst`

## Apply

```bash
git cherry-pick cb16d59854e4fa8bcbbeeed6f4938996c1763481
```

Inspect:

```bash
git show --stat cb16d59854e4fa8bcbbeeed6f4938996c1763481
git show cb16d59854e4fa8bcbbeeed6f4938996c1763481
```

## Consumption note

Use the command only for this listed technical unit; blank commands are deliberate evidence boundaries.
