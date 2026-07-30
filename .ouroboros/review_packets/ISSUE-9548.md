# Issue review unit: relationship loader options do a "recursive" thing inconsistently

- **Covered issues:** #9548
- **Review unit:** `COMMIT-626eb012e7adecec2516a20ee8a515b4e1cb6250`
- **Shape:** standalone-commit
- **Apply once:** not shared
- **Frozen base:** `aa1a5575358d3aa14953b04dced02f4763fed2e7`
- **Frozen option target:** SQLAlchemy 2.1
- **Subsystem:** ORM

## Problem and intended behavior

- **Issue #9548:** relationship loader options do a "recursive" thing inconsistently

## Scope and provenance

- **Issue #9548:** verified_local_option_closure

Changed files:

- `doc/build/changelog/unreleased_21/9548.rst`
- `doc/build/orm/queryguide/relationships.rst`
- `lib/sqlalchemy/orm/path_registry.py`
- `lib/sqlalchemy/orm/strategy_options.py`
- `test/orm/test_default_strategies.py`

Overlap summary: none identified

Exact overlap identifiers remain available in `issue_review_packet_index.jsonl`
and `evidence_bundle.json`; they are not expanded here unless needed for a
selection decision.


## Validation

No separate focused receipt is borrowed for this issue unit. Changed test files
are listed below, and the complete publication-tree validation is reported
without turning it into an issue-specific claim.

Changed test files:

- `test/orm/test_default_strategies.py`

- Non-typing suite: 25800 passed, 1502 skipped, 0 failed, 0 errors.
- Typing suite: 77 passed; its recorded failure boundary matches the frozen upstream baseline.

Changelog files:

- `doc/build/changelog/unreleased_21/9548.rst`

## Apply

```bash
git cherry-pick 626eb012e7adecec2516a20ee8a515b4e1cb6250
```

Inspect:

```bash
git show --stat 626eb012e7adecec2516a20ee8a515b4e1cb6250
git show 626eb012e7adecec2516a20ee8a515b4e1cb6250
```

## Consumption note

Use the command only for this listed technical unit; blank commands are deliberate evidence boundaries.

Questions, requested changes, preferences, and rejection reasons can be sent
through the [fork-only feedback path](../FEEDBACK.md). Include review unit
`COMMIT-626eb012e7adecec2516a20ee8a515b4e1cb6250`; no upstream mention is required.
