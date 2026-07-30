# Shared review unit: PostgreSQL schema-qualified collation reflection

- **Covered issues:** #6511, #9693
- **Review unit:** `COLLATION-SCHEMA`
- **Shape:** standalone-commit
- **Apply once:** yes
- **Frozen base:** `aa1a5575358d3aa14953b04dced02f4763fed2e7`
- **Frozen option target:** SQLAlchemy 2.0
- **Subsystem:** PostgreSQL dialect / collation DDL and reflection

## Problem and intended behavior

- **Issue #6511:** Adds PostgreSQL support for carrying an explicit collation schema through reflection and SQL or DDL rendering while keeping the representation extensible to other dialects.
- **Issue #9693:** Carries a collation schema separately from the collation name across SQL and DDL constructs, avoiding dotted-name parsing and preserving identifier quoting.

## Scope and provenance

- **Issue #6511:** Standalone frozen-base implementation option.
- **Issue #9693:** Recovered objective from earlier pull-request work.

Changed files:

- `doc/build/changelog/unreleased_20/12698.rst`
- `doc/build/changelog/unreleased_20/6511.rst`
- `doc/build/changelog/unreleased_20/9693.rst`
- `lib/sqlalchemy/dialects/postgresql/base.py`
- `lib/sqlalchemy/dialects/postgresql/named_types.py`
- `lib/sqlalchemy/sql/_elements_constructors.py`
- `lib/sqlalchemy/sql/compiler.py`
- `lib/sqlalchemy/sql/elements.py`
- `lib/sqlalchemy/sql/sqltypes.py`
- `lib/sqlalchemy/sql/type_api.py`
- `test/dialect/postgresql/test_compiler.py`
- `test/dialect/postgresql/test_reflection.py`
- `test/dialect/postgresql/test_types.py`
- `test/engine/test_reflection.py`
- `test/sql/test_compiler.py`
- `test/sql/test_operators.py`
- `test/sql/test_quote.py`
- `test/sql/test_types.py`

Overlap summary: PR packets: PR-13303, PR-13323, PR-13455, PR-13465; 8 standalone exact-file overlaps

Exact overlap identifiers remain available in `issue_review_packet_index.jsonl`
and `evidence_bundle.json`; they are not expanded here unless needed for a
selection decision.


## Current-upstream alternative

This is the frozen SQLAlchemy 2.0 option. The newer [issue 13447 review
packet](https://github.com/cjc0013/sqlalchemy/blob/ouroboros/issue-13447-review-20260730/.ouroboros/ISSUE-13447.md) carries the same problem family against a current
upstream base with an explicit collation-schema design. For new review, start
with the [current code branch](https://github.com/cjc0013/sqlalchemy/tree/ouroboros/issue-13447-20260730); retain this unit when the
older frozen-base shape is specifically useful.


## Validation

No separate focused receipt is borrowed for this issue unit. Changed test files
are listed below, and the complete publication-tree validation is reported
without turning it into an issue-specific claim.

Changed test files:

- `test/dialect/postgresql/test_compiler.py`
- `test/dialect/postgresql/test_reflection.py`
- `test/dialect/postgresql/test_types.py`
- `test/engine/test_reflection.py`
- `test/sql/test_compiler.py`
- `test/sql/test_operators.py`
- `test/sql/test_quote.py`
- `test/sql/test_types.py`

- Non-typing suite: 25800 passed, 1502 skipped, 0 failed, 0 errors.
- Typing suite: 77 passed; its recorded failure boundary matches the frozen upstream baseline.

Changelog files:

- `doc/build/changelog/unreleased_20/12698.rst`
- `doc/build/changelog/unreleased_20/6511.rst`
- `doc/build/changelog/unreleased_20/9693.rst`

## Apply

```bash
git cherry-pick da97028686f10cbceae7ea1e27480919a7b3287f
```

Inspect:

```bash
git show --stat da97028686f10cbceae7ea1e27480919a7b3287f
git show da97028686f10cbceae7ea1e27480919a7b3287f
```

## Consumption note

This command covers all listed issues. Apply it once even when entering through more than one issue row.

Questions, requested changes, preferences, and rejection reasons can be sent
through the [fork-only feedback path](../FEEDBACK.md). Include review unit
`COLLATION-SCHEMA`; no upstream mention is required.
