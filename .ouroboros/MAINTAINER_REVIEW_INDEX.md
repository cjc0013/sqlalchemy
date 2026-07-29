# Maintainer review queue

This is the human entry point for the option catalog. Each pull-request packet is sized as a coherent local review unit and carries scope, commit order, overlap, tests, changelog handling, and copy-paste inspection commands. Nothing here uploads to Gerrit or creates a GitHub pull request, issue, comment, mention, or notification.

The TSV and JSONL files remain the machine source of truth. These pages are a review layer generated from those exact rows.

## Complete accounting

- Pull-request objectives represented: 27
- Pull-request packets with direct apply commands: 26
- Issue outcomes represented: 80
- Issue rows with direct apply commands: 56 (55 unique commands)
- Standalone issue commit options: 40
- Pull-request-backed issue options: 16
- Already-present issue outcomes: 3
- Validation-only issue outcomes: 21
- PR packets with passing focused validation: 22
- PR packets with no applicable focused pytest target: 5

Issue rows and PR packets overlap: one PR can close an issue, and one commit can cover multiple issues. The counts above describe coverage and consumption paths, not an additive count of independent patches.

See `ISSUE_REVIEW_INDEX.md` for every issue outcome, including all direct commands and every evidence-only result.

## Ready for technical review (17)

- [PR 13312](review_packets/PR-13312.md) — test: add coverage for delete with nested alias exists (SQL compiler / DELETE compilation; one test commit; focused validation: passed)
- [PR 13323](review_packets/PR-13323.md) — Apply tuple bind expressions to expanding IN values (SQL expression language; one source commit; focused validation: passed)
- [PR 13368](review_packets/PR-13368.md) — Document deprecated MySQL (M,D) float syntax and improve error message (mysql dialect; one source commit; focused validation: passed)
- [PR 13404](review_packets/PR-13404.md) — Subqueryload without per-row Row construction — ~26% on subqueryload (ORM; exact integrated net delta; focused validation: passed)
- [PR 13405](review_packets/PR-13405.md) — # Cython batch instance processor — ~10–30% on most loads (collection joinedload −5%) (ORM, SQLAlchemy core; exact integrated net delta; focused validation: passed)
- [PR 13415](review_packets/PR-13415.md) — scalars/mappings performance improvement. (SQL expression language, SQLAlchemy core, asyncio extension, engine; 6 source commits; focused validation: passed)
- [PR 13416](review_packets/PR-13416.md) — Perf/eager collection bulk extend (ORM; 6 source commits; focused validation: passed)
- [PR 13435](review_packets/PR-13435.md) — Add log_note execution option (ORM, SQL expression language, asyncio extension, engine, typing; one source commit; focused validation: passed)
- [PR 13436](review_packets/PR-13436.md) — docs: document @classmethod usage with declared_attr for typing (ORM, typing; 4 source commits; focused validation: passed)
- [PR 13438](review_packets/PR-13438.md) — Homogenize declared_attr parameter name (ORM, typing; one source commit; focused validation: passed)
- [PR 13442](review_packets/PR-13442.md) — Add disconnect error handling for mssqlpython dialect (mssql dialect; 2 source commits; focused validation: passed)
- [PR 13452](review_packets/PR-13452.md) — mssql: exclude LOB types from length assignment in column reflection (mssql dialect; 3 source commits; focused validation: passed)
- [PR 13453](review_packets/PR-13453.md) — docs: add async-specific note to expire/expire_all proxied docstrings (asyncio extension; one source commit; focused validation: not applicable)
- [PR 13454](review_packets/PR-13454.md) — test(mysql): cover ordered from-select upserts (mysql dialect; one test commit; focused validation: passed)
- [PR 13456](review_packets/PR-13456.md) — docs: document sequence arguments to any_ and all_ (SQL expression language; one source commit; focused validation: not applicable)
- [PR 13457](review_packets/PR-13457.md) — Add support for multiple on-conflict clauses in inserts on SQLite (sqlite dialect; one source commit; focused validation: passed)
- [PR 13459](review_packets/PR-13459.md) — Bump pypa/cibuildwheel from 4.1.0 to 4.1.1 (build and CI; one source commit; focused validation: not applicable)

## Needs design or branch decision (9)

- [PR 11437](review_packets/PR-11437.md) — initial commit to update the SQLAlchemy examples (examples; validated patch-equivalent repair; focused validation: not applicable)
- [PR 12297](review_packets/PR-12297.md) — refactor(MSExecutionContext): improve identity insert handling and va… (mssql dialect; validated patch-equivalent repair; focused validation: passed)
- [PR 13051](review_packets/PR-13051.md) — Added implementations for avg & abs (SQL expression language, typing; validated patch-equivalent repair; focused validation: passed)
- [PR 13288](review_packets/PR-13288.md) — fix(pool): use time.monotonic() instead of time.time() for connection timestamps (connection pool; one source commit; focused validation: not applicable)
- [PR 13289](review_packets/PR-13289.md) — fix: raise clear error when default_factory/default passed to WriteOnlyMapped/DynamicMapped relationship (ORM; 3 source commits; focused validation: passed)
- [PR 13303](review_packets/PR-13303.md) — Fix PostgreSQL CHECK constraint reflection stripping unrelated parens (SQLAlchemy core, postgresql dialect, sqlite dialect; 5 source commits; focused validation: passed)
- [PR 13399](review_packets/PR-13399.md) — UniqueConstraint and Index withheld from table via attach_to_table flag, and appended to table via append_constraint (SQL expression language; 5 source commits; focused validation: passed)
- [PR 13455](review_packets/PR-13455.md) — Add postgresql_unnamed Index option to support nameless CREATE INDEX on PostgreSQL (SQL expression language, postgresql dialect; 7 source commits; focused validation: passed)
- [PR 13461](review_packets/PR-13461.md) — escape backslashes in mysql enum/set value rendering (mysql dialect; one source commit; focused validation: passed)

## Evidence only or already resolved (1)

- [PR 12731](review_packets/PR-12731.md) — fix(typing): allow DeclarativeBase subclasses in with_for_update(of=...) (SQL expression typing / with_for_update(); maintained superseding objective already present on the frozen base; focused validation: passed)

## Issue outcomes that intentionally have no patch packet

These outcomes are retained as evidence and are not missing cherry-pick commands.

- `no-pick-needed` (3): Issue 6468, Issue 10742, Issue 12341
- `validation-only` (21): Issue 4567, Issue 4784, Issue 5139, Issue 5564, Issue 5846, Issue 6084, Issue 7149, Issue 7732, Issue 8341, Issue 8693, Issue 9147, Issue 9348, Issue 9839, Issue 9930, Issue 10094, Issue 10380, Issue 10527, Issue 11284, Issue 12561, Issue 13204, Issue 13210
- `no-exact-unit` (0): None

## Gerrit handoff boundary

The catalog stops before Change-Id creation or upload. If a maintainer elects a packet, apply it locally, revise or split it as needed, run the packet's tests, add any required changelog fragment, then use the project's normal Gerrit workflow. Multi-commit packets preserve source order so a maintainer can keep a dependency chain or squash it deliberately.
