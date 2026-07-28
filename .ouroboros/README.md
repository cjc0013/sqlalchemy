# SQLAlchemy option integration - 2026-07-28

This fork publishes a reviewable option set. It does not claim upstream acceptance and it does not create or link upstream pull requests, issues, comments, or reviewer mentions.

## Start here

- Complete code branch: `ouroboros/all-20260728`
- Catalog branch: `ouroboros/catalog-20260728`
- Notification canary: `ouroboros/canary-no-notify-9425-20260728`
- Frozen upstream base: `aa1a5575358d3aa14953b04dced02f4763fed2e7`
- Validated integration head: `ac91268e679adb2c5e99ebd66e2462bbbb5ccf61`
- Notification-safe publication head: `817011f2531cbe6d939e68859b5a01a2846d3088`
- [Review the complete code diff](https://github.com/cjc0013/sqlalchemy/compare/aa1a5575358d3aa14953b04dced02f4763fed2e7...ouroboros/all-20260728)

## Coverage

- Current upstream issues represented: 182
- Issues with local closure options: 80
- Residual issues: 102
- Collapsed residual work units: 101
- Current upstream pull requests integrated locally: 27
- Commits after the frozen base: 145

## Validation

- Non-typing suite: 25800 passed, 1502 skipped, 0 failed, 0 errors.
- Typing suite: 77 passed with one failure matching the stored upstream baseline.
- Integration-only failures: 0.

## Review order

1. `MAINTAINER_REVIEW_INDEX.md` - three human review queues.
2. `review_packets/` - one Gerrit-shaped review packet per integrated pull-request option.
3. `REVIEW_GUIDE.md` - fetch, inspect, and consumption instructions.
4. `review_packet_index.jsonl` - machine mirror of packet scope, order, overlap, and decisions.
5. `pr_pick_commands.tsv` - one copy-paste command row per integrated pull request.
6. `issue_pick_commands.tsv` - issue options separated into commits, PR units, already-present behavior, and validation-only closures.
7. `commit_series.tsv` - exact commit and authorship order.
8. `pr_coverage.jsonl` - imported pull-request coverage and objective review state.
9. `issue_coverage.jsonl` - local issue closure coverage and remaining block reasons.
10. `residual_work_units.jsonl` - unresolved issues collapsed into reviewable work units.
11. `ci_attribution.jsonl` - failed-check attribution without assuming every CI failure belongs to a patch.
12. `validation_summary.json` - test counts and SHA-256 evidence.
13. `publication_manifest.json` - hashes for every catalog artifact.

## Catalog scope

This catalog is limited to technical patch provenance, issue and pull-request coverage, CI attribution, validation evidence, and local consumption instructions. Upstream issue and pull-request numbers are identifiers only and use no closing keywords or backlink-producing references.
