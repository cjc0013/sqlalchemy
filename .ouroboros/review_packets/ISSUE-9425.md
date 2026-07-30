# Issue review unit â€” tighten up compoundselect + textualselect use cases

- **Covered issues:** #9425
- **Review unit:** `COMMIT-82fd41fc014568568babf5b6868d058541173572`
- **Shape:** standalone-commit
- **Apply once:** not shared
- **Frozen base:** `aa1a5575358d3aa14953b04dced02f4763fed2e7`
- **Suggested target:** SQLAlchemy 2.1
- **Subsystem:** SQL expression language

## Problem and intended behavior

- **Issue #9425:** tighten up compoundselect + textualselect use cases.

## Scope and provenance

- Issue #9425: `verified_local_option_closure`

Changed files:

- `doc/build/changelog/unreleased_21/9425.rst`
- `lib/sqlalchemy/sql/compiler.py`
- `test/sql/test_compiler.py`

Overlapping review units: COLLATION-SCHEMA, PR-13323

## Validation

No separate focused receipt is borrowed for this issue unit. Changed test files
are listed below, and the complete publication-tree validation is reported
without turning it into an issue-specific claim.

Changed test files:

- `test/sql/test_compiler.py`

- Non-typing suite: 25800 passed, 1502 skipped, 0 failed, 0 errors.
- Typing suite: 77 passed; its recorded failure boundary matches the frozen upstream baseline.

Changelog files:

- `doc/build/changelog/unreleased_21/9425.rst`

## Apply

```bash
git cherry-pick 82fd41fc014568568babf5b6868d058541173572
```

Inspect:

```bash
git show --stat 82fd41fc014568568babf5b6868d058541173572
git show 82fd41fc014568568babf5b6868d058541173572
```

## Consumption note

Use the command only for this listed technical unit; blank commands are deliberate evidence boundaries.
