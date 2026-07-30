# Issue review unit: Always include where cluases in delete statements -- at least in test cleanup

- **Covered issues:** #6505
- **Review unit:** `COMMIT-f9cd575cde82631b4c621d46956906f1430a6eb4`
- **Shape:** standalone-commit
- **Apply once:** not shared
- **Frozen base:** `aa1a5575358d3aa14953b04dced02f4763fed2e7`
- **Frozen option target:** Maintainer choice; this unit has no changelog fragment
- **Subsystem:** SQLAlchemy core

## Problem and intended behavior

- **Issue #6505:** Always include where cluases in delete statements -- at least in test cleanup

## Scope and provenance

- **Issue #6505:** verified_local_option_closure

Changed files:

- `lib/sqlalchemy/testing/provision.py`
- `test/base/test_provision.py`

Overlap summary: none identified

Exact overlap identifiers remain available in `issue_review_packet_index.jsonl`
and `evidence_bundle.json`; they are not expanded here unless needed for a
selection decision.


## Validation

No separate focused receipt is borrowed for this issue unit. Changed test files
are listed below, and the complete publication-tree validation is reported
without turning it into an issue-specific claim.

Changed test files:

- `test/base/test_provision.py`

- Non-typing suite: 25800 passed, 1502 skipped, 0 failed, 0 errors.
- Typing suite: 77 passed; its recorded failure boundary matches the frozen upstream baseline.

Changelog files:

No issue-specific changelog file is isolated.

## Apply

```bash
git cherry-pick f9cd575cde82631b4c621d46956906f1430a6eb4
```

Inspect:

```bash
git show --stat f9cd575cde82631b4c621d46956906f1430a6eb4
git show f9cd575cde82631b4c621d46956906f1430a6eb4
```

## Consumption note

Use the command only for this listed technical unit; blank commands are deliberate evidence boundaries.

Questions, requested changes, preferences, and rejection reasons can be sent
through the [fork-only feedback path](../FEEDBACK.md). Include review unit
`COMMIT-f9cd575cde82631b4c621d46956906f1430a6eb4`; no upstream mention is required.
