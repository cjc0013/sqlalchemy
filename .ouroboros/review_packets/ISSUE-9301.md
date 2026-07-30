# Issue review unit: Support mapped attributes that have deferred definitions

- **Covered issues:** #9301
- **Review unit:** `COMMIT-bf08cd63b4401bc315d64a1f05c0b98c4d07ccec`
- **Shape:** standalone-commit
- **Apply once:** not shared
- **Frozen base:** `aa1a5575358d3aa14953b04dced02f4763fed2e7`
- **Frozen option target:** Maintainer choice; this unit has no changelog fragment
- **Subsystem:** typing

## Problem and intended behavior

- **Issue #9301:** Support mapped attributes that have deferred definitions

## Scope and provenance

- **Issue #9301:** verified_local_option_closure

Changed files:

- `doc/build/orm/mapped_sql_expr.rst`
- `test/typing/plain_files/orm/late_mapped_attribute.py`

Overlap summary: none identified

Exact overlap identifiers remain available in `issue_review_packet_index.jsonl`
and `evidence_bundle.json`; they are not expanded here unless needed for a
selection decision.


## Validation

No separate focused receipt is borrowed for this issue unit. Changed test files
are listed below, and the complete publication-tree validation is reported
without turning it into an issue-specific claim.

Changed test files:

- `test/typing/plain_files/orm/late_mapped_attribute.py`

- Non-typing suite: 25800 passed, 1502 skipped, 0 failed, 0 errors.
- Typing suite: 77 passed; its recorded failure boundary matches the frozen upstream baseline.

Changelog files:

No issue-specific changelog file is isolated.

## Apply

```bash
git cherry-pick bf08cd63b4401bc315d64a1f05c0b98c4d07ccec
```

Inspect:

```bash
git show --stat bf08cd63b4401bc315d64a1f05c0b98c4d07ccec
git show bf08cd63b4401bc315d64a1f05c0b98c4d07ccec
```

## Consumption note

Use the command only for this listed technical unit; blank commands are deliberate evidence boundaries.

Questions, requested changes, preferences, and rejection reasons can be sent
through the [fork-only feedback path](../FEEDBACK.md). Include review unit
`COMMIT-bf08cd63b4401bc315d64a1f05c0b98c4d07ccec`; no upstream mention is required.
