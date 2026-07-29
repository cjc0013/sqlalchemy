# SQLAlchemy option integration - 2026-07-28

**ONGOING WORK IN PROGRESS. IF YOU ARE LOOKING AT THIS NOW, IT IS NOT YET FINISHED. PLEASE WAIT UNTIL IT IS FINISHED TO JUDGE. THANK YOU. IT SHOULD BE FINISHED SOMETIME TODAY.**

This fork publishes a reviewable option set. It does not claim upstream acceptance and it does not create or link upstream pull requests, issues, comments, or reviewer mentions.

## Start here

- Complete code branch: `ouroboros/all-20260728`
- Catalog branch: `ouroboros/catalog-20260728`
- Notification canary: `ouroboros/canary-no-notify-9425-20260728`
- Frozen upstream base: `aa1a5575358d3aa14953b04dced02f4763fed2e7`
- Validated integration head: `c64be3b26036fcd3798ced1279b30d8440e39a82`
- Notification-safe publication head: `c64be3b26036fcd3798ced1279b30d8440e39a82`
- [Review the complete code diff](https://github.com/cjc0013/sqlalchemy/compare/aa1a5575358d3aa14953b04dced02f4763fed2e7...ouroboros/all-20260728)

## Coverage

- Current upstream issues represented: 180
- Issues with local closure options: 79
- Residual issues: 101
- Collapsed residual work units: 100
- Current upstream pull requests integrated locally: 24
- Pull-request packets with direct apply commands: 23
- Issue outcomes with direct apply commands: 55
- PR packets with passing focused validation: 21
- Commits after the frozen base: 148

## Validation

- Non-typing suite: 25800 passed, 1502 skipped, 0 failed, 0 errors.
- Typing suite: 77 passed with one failure matching the stored upstream baseline.
- Integration-only failures: 0.

## Review order

1. `MAINTAINER_REVIEW_INDEX.md` - complete accounting followed by three PR review queues.
2. `ISSUE_REVIEW_INDEX.md` - every issue outcome and direct issue command.
3. `review_packets/` - one concise Gerrit-shaped review packet per integrated pull-request option.
4. `REVIEW_GUIDE.md` - fetch, inspect, and consumption instructions.
5. `review_packet_index.jsonl` - machine mirror of packet scope, order, overlap, validation, and decisions.
6. `focused_validation.jsonl` - packet-specific commands, counts, and receipt hashes.
7. `pr_pick_commands.tsv` - one copy-paste command row per integrated pull request.
8. `issue_pick_commands.tsv` - issue options separated into commits, PR units, already-present behavior, and validation-only closures.
9. `commit_series.tsv` - exact commit and authorship order.
10. `pr_coverage.jsonl` - imported pull-request coverage and objective review state.
11. `issue_coverage.jsonl` - local issue closure coverage and remaining block reasons.
12. `residual_work_units.jsonl` - unresolved issues collapsed into reviewable work units.
13. `ci_attribution.jsonl` - failed-check attribution without assuming every CI failure belongs to a patch.
14. `validation_summary.json` - combined-suite test counts and SHA-256 evidence.
15. `publication_manifest.json` - hashes for every catalog artifact.

## Catalog scope

This catalog is limited to technical patch provenance, issue and pull-request coverage, CI attribution, validation evidence, and local consumption instructions. Upstream issue and pull-request numbers are identifiers only and use no closing keywords or backlink-producing references.
