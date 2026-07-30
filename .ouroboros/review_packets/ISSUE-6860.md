# Issue review unit: smoother with_parent() failure modes

- **Covered issues:** #6860
- **Review unit:** `COMMIT-929a60a51600654eca0b153cc968979f8b24498f`
- **Shape:** standalone-commit
- **Apply once:** not shared
- **Frozen base:** `aa1a5575358d3aa14953b04dced02f4763fed2e7`
- **Frozen option target:** SQLAlchemy 2.1
- **Subsystem:** ORM

## Problem and intended behavior

- **Issue #6860:** smoother with_parent() failure modes

## Scope and provenance

- **Issue #6860:** verified_local_option_closure

Changed files:

- `doc/build/changelog/unreleased_21/6860.rst`
- `lib/sqlalchemy/orm/util.py`
- `test/orm/test_query.py`

Overlap summary: none identified

Exact overlap identifiers remain available in `issue_review_packet_index.jsonl`
and `evidence_bundle.json`; they are not expanded here unless needed for a
selection decision.


## Validation

No separate focused receipt is borrowed for this issue unit. Changed test files
are listed below, and the complete publication-tree validation is reported
without turning it into an issue-specific claim.

Changed test files:

- `test/orm/test_query.py`

- Non-typing suite: 25800 passed, 1502 skipped, 0 failed, 0 errors.
- Typing suite: 77 passed; its recorded failure boundary matches the frozen upstream baseline.

Changelog files:

- `doc/build/changelog/unreleased_21/6860.rst`

## Apply

```bash
git cherry-pick 929a60a51600654eca0b153cc968979f8b24498f
```

Inspect:

```bash
git show --stat 929a60a51600654eca0b153cc968979f8b24498f
git show 929a60a51600654eca0b153cc968979f8b24498f
```

## Consumption note

Use the command only for this listed technical unit; blank commands are deliberate evidence boundaries.

Questions, requested changes, preferences, and rejection reasons can be sent
through the [fork-only feedback path](../FEEDBACK.md). Include review unit
`COMMIT-929a60a51600654eca0b153cc968979f8b24498f`; no upstream mention is required.
