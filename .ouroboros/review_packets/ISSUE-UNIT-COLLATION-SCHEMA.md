# Issue review unit â€” PostgreSQL schema-qualified collation reflection

- **Covered issues:** #6511, #9693
- **Review unit:** `COLLATION-SCHEMA`
- **Shape:** standalone-commit
- **Apply once:** yes
- **Frozen base:** `aa1a5575358d3aa14953b04dced02f4763fed2e7`
- **Suggested target:** SQLAlchemy 2.0
- **Subsystem:** SQL expression language, engine, postgresql dialect

## Problem and intended behavior

- **Issue #6511:** Poster at issue 6507 requested PostgreSQL however this can be implemented for as many backends as is feasible.
- **Issue #9693:** support DDL / SQL time rendering of collation schema across all constructs that include a collation

## Scope and provenance

- Issue #6511: `verified_local_option_closure`
- Issue #9693: `carried_dropped_pr_repair_objective`

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

Overlapping review units: COMMIT-0d62dfb5241d64999750e68d5896df60e47c490e, COMMIT-27f4a913f99cc99fdf40491746e78d4b71d03d3b, COMMIT-32b7e6e7e186a23923692e53faf9cb1110b620d4, COMMIT-43136535d03a5f190275ea389cb8c5fe380df672, COMMIT-483d715186d7a0d176dc749bb358861f6b31d81d, COMMIT-82fd41fc014568568babf5b6868d058541173572, COMMIT-ac07c1976b5e3860ff070c078d044995a28c3918, COMMIT-d5244bbb9527a9161a7fc08cc21d5fb240f1dd42, PR-13303, PR-13323, PR-13455, PR-13465

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
