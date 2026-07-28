# Selective review and consumption guide

Nothing in this catalog needs an upstream pull request, issue, comment, or mention. Fetch the option branch once:

```bash
git fetch https://github.com/cjc0013/sqlalchemy.git refs/heads/ouroboros/all-20260728:refs/remotes/ouroboros/options
```

## Pull-request options

`pr_pick_commands.tsv` contains one row for each of the 27 integrated pull-request options.

- `recommended_command` is the simplest safe consumption command for that row.
- `inspect_command` shows the net file-level change before applying it.
- `exact_net_command` is available when a reviewer prefers the exact integrated delta.
- Single commits and ordinary commit series preserve original commit authors. Rows containing internal merges use the exact integration delta or a squash workflow.
- Patch-equivalent rows consume a validated repair objective rather than asserting that the current source head was merged. A grouped repair may include related objectives and is labeled explicitly.

Run commands from a clean review branch based on the maintainer's current target branch. A conflict means the option overlaps newer work and should be reviewed normally; it is not evidence that the option itself is wrong.

## Issue options

`issue_pick_commands.tsv` contains all 80 locally closed issue rows:

- Standalone commit options: 40
- Pull-request-backed options: 16
- No pick needed because the behavior is already present: 3
- Validation-only closures with no isolated patch claim: 21
- Rows where the frozen evidence does not justify an exact unit: 0

Blank commands are deliberate. They prevent a branch-state validation result or already-present behavior from being presented as a patch.

## Whole option branch

To inspect the complete combined result:

```bash
git diff --stat aa1a5575358d3aa14953b04dced02f4763fed2e7...refs/remotes/ouroboros/options
```

The full branch is an option set, not an upstream acceptance or merge claim.
