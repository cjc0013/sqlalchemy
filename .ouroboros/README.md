# SQLAlchemy option integration - 2026-07-28

This fork publishes a reviewable option set. It does not claim upstream acceptance and it does not create or link upstream pull requests, issues, comments, or reviewer mentions.

## Start here

- Complete code branch: `ouroboros/all-20260728`
- Catalog branch: `ouroboros/catalog-20260728`
- Notification canary: `ouroboros/canary-no-notify-9425-20260728`
- Frozen upstream base: `aa1a5575358d3aa14953b04dced02f4763fed2e7`
- Validated integration head: `bc409096e77f338c05a9a1cef13f8ee99edd1887`
- Notification-safe publication head: `0e6736134724c2f8d975f2a51493624f934f1f92`
- [Review the complete code diff](https://github.com/cjc0013/sqlalchemy/compare/aa1a5575358d3aa14953b04dced02f4763fed2e7...ouroboros/all-20260728)

## Coverage

- Current upstream issues represented: 182
- Issues with local closure options: 80
- Residual issues: 102
- Collapsed residual work units: 101
- Current upstream pull requests integrated locally: 26
- Commits after the frozen base: 143

## Validation

- Non-typing suite: 25796 passed, 1502 skipped, 0 failed, 0 errors.
- Typing suite: 77 passed with one failure matching the stored upstream baseline.
- Integration-only failures: 0.

## Review order

1. `commit_series.tsv` - exact commit and authorship order.
2. `pr_coverage.jsonl` - imported pull-request coverage and objective review state.
3. `issue_coverage.jsonl` - local issue closure coverage and remaining block reasons.
4. `residual_work_units.jsonl` - unresolved issues collapsed into reviewable work units.
5. `ci_attribution.jsonl` - failed-check attribution without assuming every CI failure belongs to a patch.
6. `validation_summary.json` - test counts and SHA-256 evidence.
7. `publication_manifest.json` - hashes for every catalog artifact.

## Publication boundary

Private maintainer-behavior priors, internal review forecasts, workstation paths, and control-plane receipts are intentionally not published. They were decision aids, not patch evidence. Upstream issue and pull-request numbers in the ledgers are identifiers only and use no closing keywords or backlink-producing references.
