# Issue review unit: Improve documentation to make classes use the "public" module

- **Covered issues:** #8894
- **Review unit:** `COMMIT-09385c459627b0cb24d72e616bb718bd10a57e81`
- **Shape:** standalone-commit
- **Apply once:** not shared
- **Frozen base:** `aa1a5575358d3aa14953b04dced02f4763fed2e7`
- **Frozen option target:** SQLAlchemy 2.1
- **Subsystem:** documentation

## Problem and intended behavior

- **Issue #8894:** Improve documentation to make classes use the "public" module

## Scope and provenance

- **Issue #8894:** verified_local_option_closure

Changed files:

- `doc/build/changelog/changelog_07.rst`
- `doc/build/changelog/changelog_08.rst`
- `doc/build/changelog/changelog_09.rst`
- `doc/build/changelog/changelog_10.rst`
- `doc/build/changelog/migration_11.rst`
- `doc/build/changelog/unreleased_21/8894.rst`
- `doc/build/conf.py`
- `doc/build/core/connections.rst`
- `doc/build/core/constraints.rst`
- `doc/build/core/custom_types.rst`
- `doc/build/core/ddl.rst`
- `doc/build/core/defaults.rst`
- `doc/build/core/dml.rst`
- `doc/build/core/engines.rst`
- `doc/build/core/internals.rst`
- `doc/build/core/metadata.rst`
- `doc/build/core/pooling.rst`
- `doc/build/core/reflection.rst`
- `doc/build/core/schema.rst`
- `doc/build/orm/extensions/asyncio.rst`
- `doc/build/orm/persistence_techniques.rst`

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

- `doc/build/changelog/changelog_07.rst`
- `doc/build/changelog/changelog_08.rst`
- `doc/build/changelog/changelog_09.rst`
- `doc/build/changelog/changelog_10.rst`
- `doc/build/changelog/migration_11.rst`
- `doc/build/changelog/unreleased_21/8894.rst`

## Apply

```bash
git cherry-pick 09385c459627b0cb24d72e616bb718bd10a57e81
```

Inspect:

```bash
git show --stat 09385c459627b0cb24d72e616bb718bd10a57e81
git show 09385c459627b0cb24d72e616bb718bd10a57e81
```

## Consumption note

Use the command only for this listed technical unit; blank commands are deliberate evidence boundaries.

Questions, requested changes, preferences, and rejection reasons can be sent
through the [fork-only feedback path](../FEEDBACK.md). Include review unit
`COMMIT-09385c459627b0cb24d72e616bb718bd10a57e81`; no upstream mention is required.
