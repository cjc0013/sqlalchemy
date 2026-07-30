# SQLAlchemy maintainer option catalog - 2026-07-30

This fork collects **possible fixes** that SQLAlchemy maintainers can inspect,
test, cherry-pick, revise, or decline. The goal is simple: reduce maintainer
workload by doing the implementation and evidence-gathering work up front.

These packets are not claims of upstream acceptance or perfection. Some may be
ready unchanged; others may need a maintainer's preferred shape. No upstream
pull request, issue, comment, or reviewer mention is created by this catalog.

Nothing in this repository modifies or notifies upstream unless a maintainer
explicitly chooses to adopt a change.

## Start here

- **[Unified maintainer evidence hub](EVIDENCE_HUB.md)**
- Catalog release: `20260730.3`
- Complete code branch: `ouroboros/all-20260728`
- Catalog branch: `ouroboros/catalog-20260728`
- Notification canary: `ouroboros/canary-no-notify-9425-20260728`
- Frozen upstream base: `aa1a5575358d3aa14953b04dced02f4763fed2e7`
- Validated integration head: `c64be3b26036fcd3798ced1279b30d8440e39a82`
- Notification-safe publication head: `c64be3b26036fcd3798ced1279b30d8440e39a82`
- [Review the complete code diff](https://github.com/cjc0013/sqlalchemy/compare/aa1a5575358d3aa14953b04dced02f4763fed2e7...ouroboros/all-20260728)

## Current option: issue 13447

The newest option provides PostgreSQL schema-qualified collation support against
a current upstream base. It is newer than the frozen catalog below and is the
preferred starting point for this problem family.

Its validation is reported separately from the frozen catalog in the unified
evidence hub.

- [Human review packet](https://github.com/cjc0013/sqlalchemy/blob/ouroboros/issue-13447-review-20260730/.ouroboros/ISSUE-13447.md)
- [Clean code branch](https://github.com/cjc0013/sqlalchemy/tree/ouroboros/issue-13447-20260730)
- Code head: `9eb6026dad03a987f891af03395f6eb49260edbd`
- Apply: `git cherry-pick 7836a24696b6592594827f7f23391af4eb39c163 cb0d965aa39a1cfb23c730b985c96c091f40d690 9eb6026dad03a987f891af03395f6eb49260edbd`

## Frozen catalog coverage

- Current upstream issues represented: 180
- Issues with local closure options: 79
- Residual issues: 101
- Collapsed residual work units: 100
- Current upstream pull requests integrated locally: 24
- Pull-request packets with direct apply commands: 23
- Issue outcomes with direct apply commands: 51
- Unique transferable issue units: 50
- PR packets with passing focused validation: 21
- Commits after the frozen base: 148

## Frozen catalog validation

- Non-typing suite: 25800 passed, 1502 skipped, 0 failed, 0 errors.
- Typing suite: 77 passed with one failure matching the stored upstream baseline.
- Integration-only failures: 0.

## Review order

1. `EVIDENCE_HUB.md` - one human entry point for purpose, current work, evidence, and feedback.
2. `MAINTAINER_REVIEW_INDEX.md` - complete accounting followed by three PR review queues.
3. `ISSUE_REVIEW_INDEX.md` - every issue outcome and direct issue command.
4. `review_packets/` - concise Gerrit-shaped PR packets and human-readable issue outcome packets.
5. `evidence_bundle.json` - one machine-readable join across packets, commands, validation, coverage, and feedback.
6. `FEEDBACK.md` and `feedback_contract.json` - fork-only maintainer feedback and Ouroboros ingestion contract.
7. `REVIEW_GUIDE.md` - fetch, inspect, and consumption instructions.
8. `publication_manifest.json` - hashes for every catalog artifact.

The detailed JSONL and TSV evidence remains available for exact packet routing,
focused validation, commit order, CI attribution, coverage, and residual work.

## Feedback and change policy

Each release is an immutable, usable snapshot. Feedback may produce a new
release without altering the previous one. Maintainer interaction is optional,
and every exact commit remains cherry-pickable.

If maintainers ask questions or request changes, the next release can revise the
relevant option while preserving the old commit and receipt trail. Use the
[fork-only feedback path](FEEDBACK.md); it does not require an upstream comment
or mention.

## Catalog scope

This catalog is limited to technical patch provenance, issue and pull-request
coverage, CI attribution, validation evidence, local consumption instructions,
and fork-only feedback. Upstream identifiers use no closing keywords or
backlink-producing references.
