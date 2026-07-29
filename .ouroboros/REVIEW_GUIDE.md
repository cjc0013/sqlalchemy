# Selective review and consumption guide

Nothing in this catalog needs an upstream pull request, issue, comment, or mention. Fetch the option branch once:

```bash
git fetch https://github.com/cjc0013/sqlalchemy.git refs/heads/ouroboros/all-20260728:refs/remotes/ouroboros/options
```

Start with `MAINTAINER_REVIEW_INDEX.md`. It accounts for every PR and issue outcome, then separates coherent technical-review units, units that still need a design or branch decision, and evidence-only outcomes. `ISSUE_REVIEW_INDEX.md` lists every issue result and every direct issue command.

## Pull-request options

`pr_pick_commands.tsv` contains one row for each of the 24 integrated pull-request options.

- `recommended_command` is the simplest safe consumption command for that row.
- `inspect_command` shows the net file-level change before applying it.
- `integrated_reproduction_command` is secondary and reproduces the combined integration-branch delta when it differs from the original commit path.
- Original commits are the primary path whenever they apply cleanly from the frozen base. Merge-delta commands remain primary only where the original internal-merge series does not apply independently.
- Patch-equivalent rows consume a validated repair objective rather than asserting that the current source head was merged. Exact-file overlap alone is never treated as patch equivalence.

Each packet reports fresh focused validation when a runnable changed pytest target exists. A packet says `passed` only when its command has a receipt tied to the publication tree. Docs, examples, workflow-only, or otherwise non-runnable packets say `not applicable` rather than borrowing the combined-suite result.

Run commands from a clean review branch based on the maintainer's current target branch. A conflict means the option overlaps newer work and should be reviewed normally; it is not evidence that the option itself is wrong.

## Issue options

`issue_pick_commands.tsv` contains all 79 locally closed issue rows:

- Standalone commit options: 36
- Pull-request-backed options: 15
- No pick needed because the behavior is already present: 3
- Validation-only closures with no isolated patch claim: 21
- Rows where the frozen evidence does not justify an exact unit: 4

Blank commands are deliberate. They prevent a branch-state validation result or already-present behavior from being presented as a patch.

## Gerrit workflow boundary

SQLAlchemy accepts GitHub pull requests as intake and uses Gerrit for accepted code changes. This catalog prepares local review units for that workflow without uploading them. It intentionally creates no Change-Ids and assigns no reviewers or topics. If a maintainer selects a packet, apply it to the chosen target branch, revise or split it as needed, rerun its tests, make the changelog decision explicit, and then use the project's normal Gerrit commands.

Multi-commit packets preserve source order. A packet with exact-file overlaps lists the other affected review units so maintainers can choose a parent chain, a shared topic, a squash, or only one competing option deliberately.

## Whole option branch

To inspect the complete combined result:

```bash
git diff --stat aa1a5575358d3aa14953b04dced02f4763fed2e7...refs/remotes/ouroboros/options
```

The full branch is an option set, not an upstream acceptance or merge claim.
