# Issue review unit: Make the new PG Range aware of the its bounds data type

- **Covered issues:** #8936
- **Review unit:** `COMMIT-32b7e6e7e186a23923692e53faf9cb1110b620d4`
- **Shape:** standalone-commit
- **Apply once:** not shared
- **Frozen base:** `aa1a5575358d3aa14953b04dced02f4763fed2e7`
- **Frozen option target:** SQLAlchemy 2.1
- **Subsystem:** postgresql dialect

## Problem and intended behavior

- **Issue #8936:** Make the new PG Range aware of the its bounds data type

## Scope and provenance

- **Issue #8936:** verified_local_option_closure

Changed files:

- `doc/build/changelog/unreleased_21/8936.rst`
- `lib/sqlalchemy/dialects/postgresql/ranges.py`
- `test/dialect/postgresql/test_types.py`

Overlap summary: none identified

Exact overlap identifiers remain available in `issue_review_packet_index.jsonl`
and `evidence_bundle.json`; they are not expanded here unless needed for a
selection decision.


## Validation

No separate focused receipt is borrowed for this issue unit. Changed test files
are listed below, and the complete publication-tree validation is reported
without turning it into an issue-specific claim.

Changed test files:

- `test/dialect/postgresql/test_types.py`

- Non-typing suite: 25800 passed, 1502 skipped, 0 failed, 0 errors.
- Typing suite: 77 passed; its recorded failure boundary matches the frozen upstream baseline.

Changelog files:

- `doc/build/changelog/unreleased_21/8936.rst`

## Apply

```bash
git cherry-pick 32b7e6e7e186a23923692e53faf9cb1110b620d4
```

Inspect:

```bash
git show --stat 32b7e6e7e186a23923692e53faf9cb1110b620d4
git show 32b7e6e7e186a23923692e53faf9cb1110b620d4
```

## Consumption note

Use the command only for this listed technical unit; blank commands are deliberate evidence boundaries.

Questions, requested changes, preferences, and rejection reasons can be sent
through the [fork-only feedback path](../FEEDBACK.md). Include review unit
`COMMIT-32b7e6e7e186a23923692e53faf9cb1110b620d4`; no upstream mention is required.
