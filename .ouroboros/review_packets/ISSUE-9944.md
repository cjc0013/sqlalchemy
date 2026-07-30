# Issue review unit: Reflect don't recognize foreign tables in postgresql

- **Covered issues:** #9944
- **Review unit:** `COMMIT-483d715186d7a0d176dc749bb358861f6b31d81d`
- **Shape:** standalone-commit
- **Apply once:** not shared
- **Frozen base:** `aa1a5575358d3aa14953b04dced02f4763fed2e7`
- **Frozen option target:** SQLAlchemy 2.1
- **Subsystem:** postgresql dialect

## Problem and intended behavior

- **Issue #9944:** Reflect don't recognize foreign tables in postgresql

## Scope and provenance

- **Issue #9944:** verified_local_option_closure

Changed files:

- `doc/build/changelog/unreleased_21/9944.rst`
- `lib/sqlalchemy/dialects/postgresql/base.py`

Overlap summary: PR packets: PR-13303, PR-13455

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

- `doc/build/changelog/unreleased_21/9944.rst`

## Apply

```bash
git cherry-pick 483d715186d7a0d176dc749bb358861f6b31d81d
```

Inspect:

```bash
git show --stat 483d715186d7a0d176dc749bb358861f6b31d81d
git show 483d715186d7a0d176dc749bb358861f6b31d81d
```

## Consumption note

Use the command only for this listed technical unit; blank commands are deliberate evidence boundaries.

Questions, requested changes, preferences, and rejection reasons can be sent
through the [fork-only feedback path](../FEEDBACK.md). Include review unit
`COMMIT-483d715186d7a0d176dc749bb358861f6b31d81d`; no upstream mention is required.
