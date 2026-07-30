# Issue review unit: replace use of the term "primary key identifier" with "identity key" for ORM documentation / methods that refer to the identity map

- **Covered issues:** #7360
- **Review unit:** `COMMIT-2a8d83a114a17208b2430d3f3c4ce39f23338daa`
- **Shape:** standalone-commit
- **Apply once:** not shared
- **Frozen base:** `aa1a5575358d3aa14953b04dced02f4763fed2e7`
- **Frozen option target:** SQLAlchemy 2.1
- **Subsystem:** ORM

## Problem and intended behavior

- **Issue #7360:** replace use of the term "primary key identifier" with "identity key" for ORM documentation / methods that refer to the identity map

## Scope and provenance

- **Issue #7360:** verified_local_option_closure

Changed files:

- `doc/build/changelog/unreleased_21/7360.rst`
- `lib/sqlalchemy/orm/exc.py`
- `lib/sqlalchemy/orm/query.py`
- `lib/sqlalchemy/orm/scoping.py`
- `lib/sqlalchemy/orm/session.py`

Overlap summary: none identified

Exact overlap identifiers remain available in `issue_review_packet_index.jsonl`
and `evidence_bundle.json`; they are not expanded here unless needed for a
selection decision.


## Validation

No separate focused receipt is borrowed for this issue unit. Changed test files
are listed below, and the complete publication-tree validation is reported
without turning it into an issue-specific claim.

Changed test files:

No issue-specific test file is isolated.

- Non-typing suite: 25800 passed, 1502 skipped, 0 failed, 0 errors.
- Typing suite: 77 passed; its recorded failure boundary matches the frozen upstream baseline.

Changelog files:

- `doc/build/changelog/unreleased_21/7360.rst`

## Apply

```bash
git cherry-pick 2a8d83a114a17208b2430d3f3c4ce39f23338daa
```

Inspect:

```bash
git show --stat 2a8d83a114a17208b2430d3f3c4ce39f23338daa
git show 2a8d83a114a17208b2430d3f3c4ce39f23338daa
```

## Consumption note

Use the command only for this listed technical unit; blank commands are deliberate evidence boundaries.

Questions, requested changes, preferences, and rejection reasons can be sent
through the [fork-only feedback path](../FEEDBACK.md). Include review unit
`COMMIT-2a8d83a114a17208b2430d3f3c4ce39f23338daa`; no upstream mention is required.
