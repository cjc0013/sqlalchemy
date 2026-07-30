# Issue review unit â€” Please work harder to figure out parameter types for sequences

- **Covered issues:** #6874
- **Review unit:** `COMMIT-27f4a913f99cc99fdf40491746e78d4b71d03d3b`
- **Shape:** standalone-commit
- **Apply once:** not shared
- **Frozen base:** `aa1a5575358d3aa14953b04dced02f4763fed2e7`
- **Suggested target:** SQLAlchemy 2.1
- **Subsystem:** SQL expression language

## Problem and intended behavior

- **Issue #6874:** Please work harder to figure out parameter types for sequences

## Scope and provenance

- Issue #6874: `verified_local_option_closure`

Changed files:

- `doc/build/changelog/unreleased_21/6874.rst`
- `lib/sqlalchemy/sql/elements.py`
- `test/sql/test_types.py`

Overlapping review units: COLLATION-SCHEMA, COMMIT-d5244bbb9527a9161a7fc08cc21d5fb240f1dd42

## Validation

No separate focused receipt is borrowed for this issue unit. Changed test files
are listed below, and the complete publication-tree validation is reported
without turning it into an issue-specific claim.

Changed test files:

- `test/sql/test_types.py`

- Non-typing suite: 25800 passed, 1502 skipped, 0 failed, 0 errors.
- Typing suite: 77 passed; its recorded failure boundary matches the frozen upstream baseline.

Changelog files:

- `doc/build/changelog/unreleased_21/6874.rst`

## Apply

```bash
git cherry-pick 27f4a913f99cc99fdf40491746e78d4b71d03d3b
```

Inspect:

```bash
git show --stat 27f4a913f99cc99fdf40491746e78d4b71d03d3b
git show 27f4a913f99cc99fdf40491746e78d4b71d03d3b
```

## Consumption note

Use the command only for this listed technical unit; blank commands are deliberate evidence boundaries.
