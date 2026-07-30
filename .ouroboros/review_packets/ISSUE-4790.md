# Issue review unit: Improve error messages on create_table

- **Covered issues:** #4790
- **Review unit:** `COMMIT-70e6b730b53852e27ec5699f6309eba92e820c8c`
- **Shape:** standalone-commit
- **Apply once:** not shared
- **Frozen base:** `aa1a5575358d3aa14953b04dced02f4763fed2e7`
- **Frozen option target:** SQLAlchemy 2.1
- **Subsystem:** SQL expression language

## Problem and intended behavior

- **Issue #4790:** Improve error messages on create_table

## Scope and provenance

- **Issue #4790:** verified_local_option_closure

Changed files:

- `doc/build/changelog/unreleased_21/4790.rst`
- `lib/sqlalchemy/sql/naming.py`
- `test/sql/test_metadata.py`

Overlap summary: 1 standalone exact-file overlap

Exact overlap identifiers remain available in `issue_review_packet_index.jsonl`
and `evidence_bundle.json`; they are not expanded here unless needed for a
selection decision.


## Validation

No separate focused receipt is borrowed for this issue unit. Changed test files
are listed below, and the complete publication-tree validation is reported
without turning it into an issue-specific claim.

Changed test files:

- `test/sql/test_metadata.py`

- Non-typing suite: 25800 passed, 1502 skipped, 0 failed, 0 errors.
- Typing suite: 77 passed; its recorded failure boundary matches the frozen upstream baseline.

Changelog files:

- `doc/build/changelog/unreleased_21/4790.rst`

## Apply

```bash
git cherry-pick 70e6b730b53852e27ec5699f6309eba92e820c8c
```

Inspect:

```bash
git show --stat 70e6b730b53852e27ec5699f6309eba92e820c8c
git show 70e6b730b53852e27ec5699f6309eba92e820c8c
```

## Consumption note

Use the command only for this listed technical unit; blank commands are deliberate evidence boundaries.

Questions, requested changes, preferences, and rejection reasons can be sent
through the [fork-only feedback path](../FEEDBACK.md). Include review unit
`COMMIT-70e6b730b53852e27ec5699f6309eba92e820c8c`; no upstream mention is required.
