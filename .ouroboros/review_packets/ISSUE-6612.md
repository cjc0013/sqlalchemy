# Issue review unit: Cannot build SQL expression NOT(x IS NULL) on Postgres

- **Covered issues:** #6612
- **Review unit:** `COMMIT-d5244bbb9527a9161a7fc08cc21d5fb240f1dd42`
- **Shape:** standalone-commit
- **Apply once:** not shared
- **Frozen base:** `aa1a5575358d3aa14953b04dced02f4763fed2e7`
- **Frozen option target:** SQLAlchemy 2.1
- **Subsystem:** SQL expression language

## Problem and intended behavior

- **Issue #6612:** Cannot build SQL expression NOT(x IS NULL) on Postgres

## Scope and provenance

- **Issue #6612:** verified_local_option_closure

Changed files:

- `doc/build/changelog/unreleased_21/6612.rst`
- `lib/sqlalchemy/sql/elements.py`
- `lib/sqlalchemy/sql/sqltypes.py`
- `test/sql/test_operators.py`

Overlap summary: 3 standalone exact-file overlaps

Exact overlap identifiers remain available in `issue_review_packet_index.jsonl`
and `evidence_bundle.json`; they are not expanded here unless needed for a
selection decision.


## Validation

No separate focused receipt is borrowed for this issue unit. Changed test files
are listed below, and the complete publication-tree validation is reported
without turning it into an issue-specific claim.

Changed test files:

- `test/sql/test_operators.py`

- Non-typing suite: 25800 passed, 1502 skipped, 0 failed, 0 errors.
- Typing suite: 77 passed; its recorded failure boundary matches the frozen upstream baseline.

Changelog files:

- `doc/build/changelog/unreleased_21/6612.rst`

## Apply

```bash
git cherry-pick d5244bbb9527a9161a7fc08cc21d5fb240f1dd42
```

Inspect:

```bash
git show --stat d5244bbb9527a9161a7fc08cc21d5fb240f1dd42
git show d5244bbb9527a9161a7fc08cc21d5fb240f1dd42
```

## Consumption note

Use the command only for this listed technical unit; blank commands are deliberate evidence boundaries.

Questions, requested changes, preferences, and rejection reasons can be sent
through the [fork-only feedback path](../FEEDBACK.md). Include review unit
`COMMIT-d5244bbb9527a9161a7fc08cc21d5fb240f1dd42`; no upstream mention is required.
