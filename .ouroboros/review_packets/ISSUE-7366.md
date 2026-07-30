# Issue review unit â€” extend_existing will add copies of indexes, constraints, etc. as there is no deduplication on name

- **Covered issues:** #7366
- **Review unit:** `COMMIT-43136535d03a5f190275ea389cb8c5fe380df672`
- **Shape:** standalone-commit
- **Apply once:** not shared
- **Frozen base:** `aa1a5575358d3aa14953b04dced02f4763fed2e7`
- **Suggested target:** SQLAlchemy 2.1
- **Subsystem:** engine

## Problem and intended behavior

- **Issue #7366:** extend_existing will add copies of indexes, constraints, etc. as there is no deduplication on name

## Scope and provenance

- Issue #7366: `verified_local_option_closure`

Changed files:

- `doc/build/changelog/unreleased_21/7366.rst`
- `lib/sqlalchemy/engine/reflection.py`
- `test/engine/test_reflection.py`

Overlapping review units: COLLATION-SCHEMA

## Validation

No separate focused receipt is borrowed for this issue unit. Changed test files
are listed below, and the complete publication-tree validation is reported
without turning it into an issue-specific claim.

Changed test files:

- `test/engine/test_reflection.py`

- Non-typing suite: 25800 passed, 1502 skipped, 0 failed, 0 errors.
- Typing suite: 77 passed; its recorded failure boundary matches the frozen upstream baseline.

Changelog files:

- `doc/build/changelog/unreleased_21/7366.rst`

## Apply

```bash
git cherry-pick 43136535d03a5f190275ea389cb8c5fe380df672
```

Inspect:

```bash
git show --stat 43136535d03a5f190275ea389cb8c5fe380df672
git show 43136535d03a5f190275ea389cb8c5fe380df672
```

## Consumption note

Use the command only for this listed technical unit; blank commands are deliberate evidence boundaries.
