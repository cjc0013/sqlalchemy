# Issue review unit: add additional type migration section to whatsnew detailing declared_attr format changes, others

- **Covered issues:** #9212
- **Review unit:** `COMMIT-a184b039a48fc3b993346be39277cf58c64ade41`
- **Shape:** standalone-commit
- **Apply once:** not shared
- **Frozen base:** `aa1a5575358d3aa14953b04dced02f4763fed2e7`
- **Frozen option target:** Maintainer choice; this unit has no changelog fragment
- **Subsystem:** documentation

## Problem and intended behavior

- **Issue #9212:** add additional type migration section to whatsnew detailing declared_attr format changes, others

## Scope and provenance

- **Issue #9212:** verified_local_option_closure

Changed files:

- `doc/build/changelog/whatsnew_20.rst`

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

- `doc/build/changelog/whatsnew_20.rst`

## Apply

```bash
git cherry-pick a184b039a48fc3b993346be39277cf58c64ade41
```

Inspect:

```bash
git show --stat a184b039a48fc3b993346be39277cf58c64ade41
git show a184b039a48fc3b993346be39277cf58c64ade41
```

## Consumption note

Use the command only for this listed technical unit; blank commands are deliberate evidence boundaries.

Questions, requested changes, preferences, and rejection reasons can be sent
through the [fork-only feedback path](../FEEDBACK.md). Include review unit
`COMMIT-a184b039a48fc3b993346be39277cf58c64ade41`; no upstream mention is required.
