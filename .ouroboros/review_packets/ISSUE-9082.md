# Issue review unit â€” eager_defaults shouldn't be needed for pk returning even if cols are not actual pks

- **Covered issues:** #9082
- **Review unit:** `COMMIT-019dfdaddee18c126a416ae920debc966400e68b`
- **Shape:** standalone-commit
- **Apply once:** not shared
- **Frozen base:** `aa1a5575358d3aa14953b04dced02f4763fed2e7`
- **Suggested target:** SQLAlchemy 2.1
- **Subsystem:** ORM

## Problem and intended behavior

- **Issue #9082:** eager_defaults shouldn't be needed for pk returning even if cols are not actual pks

## Scope and provenance

- Issue #9082: `verified_local_option_closure`

Changed files:

- `doc/build/changelog/unreleased_21/9082.rst`
- `lib/sqlalchemy/orm/persistence.py`
- `test/orm/test_defaults.py`

Overlapping review units: COMMIT-cb16d59854e4fa8bcbbeeed6f4938996c1763481

## Validation

No separate focused receipt is borrowed for this issue unit. Changed test files
are listed below, and the complete publication-tree validation is reported
without turning it into an issue-specific claim.

Changed test files:

- `test/orm/test_defaults.py`

- Non-typing suite: 25800 passed, 1502 skipped, 0 failed, 0 errors.
- Typing suite: 77 passed; its recorded failure boundary matches the frozen upstream baseline.

Changelog files:

- `doc/build/changelog/unreleased_21/9082.rst`

## Apply

```bash
git cherry-pick 019dfdaddee18c126a416ae920debc966400e68b
```

Inspect:

```bash
git show --stat 019dfdaddee18c126a416ae920debc966400e68b
git show 019dfdaddee18c126a416ae920debc966400e68b
```

## Consumption note

Use the command only for this listed technical unit; blank commands are deliberate evidence boundaries.
