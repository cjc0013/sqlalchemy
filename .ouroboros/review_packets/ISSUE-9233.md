# Issue review unit: Expression index does not list all the columns

- **Covered issues:** #9233
- **Review unit:** `COMMIT-c004cf4aabfa967ae4a38f2569b318b0de4923db`
- **Shape:** standalone-commit
- **Apply once:** not shared
- **Frozen base:** `aa1a5575358d3aa14953b04dced02f4763fed2e7`
- **Frozen option target:** SQLAlchemy 2.1
- **Subsystem:** SQL expression language

## Problem and intended behavior

- **Issue #9233:** Expression index does not list all the columns

## Scope and provenance

- **Issue #9233:** verified_local_option_closure

Changed files:

- `doc/build/changelog/unreleased_21/9233.rst`
- `lib/sqlalchemy/sql/schema.py`
- `test/sql/test_constraints.py`

Overlap summary: PR packets: PR-13399

Exact overlap identifiers remain available in `issue_review_packet_index.jsonl`
and `evidence_bundle.json`; they are not expanded here unless needed for a
selection decision.


## Validation

No separate focused receipt is borrowed for this issue unit. Changed test files
are listed below, and the complete publication-tree validation is reported
without turning it into an issue-specific claim.

Changed test files:

- `test/sql/test_constraints.py`

- Non-typing suite: 25800 passed, 1502 skipped, 0 failed, 0 errors.
- Typing suite: 77 passed; its recorded failure boundary matches the frozen upstream baseline.

Changelog files:

- `doc/build/changelog/unreleased_21/9233.rst`

## Apply

```bash
git cherry-pick c004cf4aabfa967ae4a38f2569b318b0de4923db
```

Inspect:

```bash
git show --stat c004cf4aabfa967ae4a38f2569b318b0de4923db
git show c004cf4aabfa967ae4a38f2569b318b0de4923db
```

## Consumption note

Use the command only for this listed technical unit; blank commands are deliberate evidence boundaries.

Questions, requested changes, preferences, and rejection reasons can be sent
through the [fork-only feedback path](../FEEDBACK.md). Include review unit
`COMMIT-c004cf4aabfa967ae4a38f2569b318b0de4923db`; no upstream mention is required.
