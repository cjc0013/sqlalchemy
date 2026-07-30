# Issue review unit â€” Documentation: use ORM declarative attributes in .values instead of kwargs in "ORM-enabled UPDATE statements"?

- **Covered issues:** #6332
- **Review unit:** `COMMIT-6f8bb8dc84b27dc8bd9e5048de3d1d5152ddb132`
- **Shape:** standalone-commit
- **Apply once:** not shared
- **Frozen base:** `aa1a5575358d3aa14953b04dced02f4763fed2e7`
- **Suggested target:** Maintainer choice; this unit has no changelog fragment
- **Subsystem:** SQL expression language

## Problem and intended behavior

- **Issue #6332:** Documentation: use ORM declarative attributes in .values instead of kwargs in "ORM-enabled UPDATE statements"?

## Scope and provenance

- Issue #6332: `verified_local_option_closure`

Changed files:

- `doc/build/orm/queryguide/dml.rst`
- `lib/sqlalchemy/sql/dml.py`

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
git cherry-pick 6f8bb8dc84b27dc8bd9e5048de3d1d5152ddb132
```

Inspect:

```bash
git show --stat 6f8bb8dc84b27dc8bd9e5048de3d1d5152ddb132
git show 6f8bb8dc84b27dc8bd9e5048de3d1d5152ddb132
```

## Consumption note

Use the command only for this listed technical unit; blank commands are deliberate evidence boundaries.
