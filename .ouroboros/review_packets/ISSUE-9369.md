# Issue review unit â€” allow_unmapped seems to not be honored in all cases

- **Covered issues:** #9369
- **Review unit:** `COMMIT-f22279bfce1370cca4801a6b14119ac0833f9a84`
- **Shape:** standalone-commit
- **Apply once:** not shared
- **Frozen base:** `aa1a5575358d3aa14953b04dced02f4763fed2e7`
- **Suggested target:** SQLAlchemy 2.1
- **Subsystem:** ORM

## Problem and intended behavior

- **Issue #9369:** allow_unmapped seems to not be honored in all cases

## Scope and provenance

- Issue #9369: `verified_local_option_closure`

Changed files:

- `doc/build/changelog/unreleased_21/9369.rst`
- `lib/sqlalchemy/orm/decl_base.py`
- `test/orm/declarative/test_tm_future_annotations_sync.py`
- `test/orm/declarative/test_typed_mapping.py`

Overlapping review units: PR-13289

## Validation

No separate focused receipt is borrowed for this issue unit. Changed test files
are listed below, and the complete publication-tree validation is reported
without turning it into an issue-specific claim.

Changed test files:

- `test/orm/declarative/test_tm_future_annotations_sync.py`
- `test/orm/declarative/test_typed_mapping.py`

- Non-typing suite: 25800 passed, 1502 skipped, 0 failed, 0 errors.
- Typing suite: 77 passed; its recorded failure boundary matches the frozen upstream baseline.

Changelog files:

- `doc/build/changelog/unreleased_21/9369.rst`

## Apply

```bash
git cherry-pick f22279bfce1370cca4801a6b14119ac0833f9a84
```

Inspect:

```bash
git show --stat f22279bfce1370cca4801a6b14119ac0833f9a84
git show f22279bfce1370cca4801a6b14119ac0833f9a84
```

## Consumption note

Use the command only for this listed technical unit; blank commands are deliberate evidence boundaries.
