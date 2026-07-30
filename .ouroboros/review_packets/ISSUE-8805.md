# Issue review unit â€” Some tests for dialect ignores lack of support of CHECK CONSTRAINT

- **Covered issues:** #8805
- **Review unit:** `COMMIT-8ed8f153ee55da01b8c2667d5b87460bf2b2053f`
- **Shape:** standalone-commit
- **Apply once:** not shared
- **Frozen base:** `aa1a5575358d3aa14953b04dced02f4763fed2e7`
- **Suggested target:** SQLAlchemy 2.1
- **Subsystem:** documentation

## Problem and intended behavior

- **Issue #8805:** Some tests for dialect ignores lack of support of CHECK CONSTRAINT

## Scope and provenance

- Issue #8805: `verified_local_option_closure`

Changed files:

- `README.dialects.rst`
- `doc/build/changelog/unreleased_21/8805.rst`

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

- `doc/build/changelog/unreleased_21/8805.rst`

## Apply

```bash
git cherry-pick 8ed8f153ee55da01b8c2667d5b87460bf2b2053f
```

Inspect:

```bash
git show --stat 8ed8f153ee55da01b8c2667d5b87460bf2b2053f
git show 8ed8f153ee55da01b8c2667d5b87460bf2b2053f
```

## Consumption note

Use the command only for this listed technical unit; blank commands are deliberate evidence boundaries.
