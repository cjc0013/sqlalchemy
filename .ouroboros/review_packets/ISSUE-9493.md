# Issue review unit: MappedAsDataclass inherits dataclasses attributes, while the spec says they don't

- **Covered issues:** #9493
- **Review unit:** `COMMIT-245794ed686f9e165121f7e53d69fbcd806b2b45`
- **Shape:** standalone-commit
- **Apply once:** not shared
- **Frozen base:** `aa1a5575358d3aa14953b04dced02f4763fed2e7`
- **Frozen option target:** SQLAlchemy 2.1
- **Subsystem:** ORM

## Problem and intended behavior

- **Issue #9493:** MappedAsDataclass inherits dataclasses attributes, while the spec says they don't

## Scope and provenance

- **Issue #9493:** verified_local_option_closure

Changed files:

- `doc/build/changelog/unreleased_21/9493.rst`
- `lib/sqlalchemy/orm/decl_api.py`
- `test/orm/declarative/test_dc_transforms.py`
- `test/orm/declarative/test_dc_transforms_future_anno_sync.py`

Overlap summary: PR packets: PR-13436

Exact overlap identifiers remain available in `issue_review_packet_index.jsonl`
and `evidence_bundle.json`; they are not expanded here unless needed for a
selection decision.


## Validation

No separate focused receipt is borrowed for this issue unit. Changed test files
are listed below, and the complete publication-tree validation is reported
without turning it into an issue-specific claim.

Changed test files:

- `test/orm/declarative/test_dc_transforms.py`
- `test/orm/declarative/test_dc_transforms_future_anno_sync.py`

- Non-typing suite: 25800 passed, 1502 skipped, 0 failed, 0 errors.
- Typing suite: 77 passed; its recorded failure boundary matches the frozen upstream baseline.

Changelog files:

- `doc/build/changelog/unreleased_21/9493.rst`

## Apply

```bash
git cherry-pick 245794ed686f9e165121f7e53d69fbcd806b2b45
```

Inspect:

```bash
git show --stat 245794ed686f9e165121f7e53d69fbcd806b2b45
git show 245794ed686f9e165121f7e53d69fbcd806b2b45
```

## Consumption note

Use the command only for this listed technical unit; blank commands are deliberate evidence boundaries.

Questions, requested changes, preferences, and rejection reasons can be sent
through the [fork-only feedback path](../FEEDBACK.md). Include review unit
`COMMIT-245794ed686f9e165121f7e53d69fbcd806b2b45`; no upstream mention is required.
