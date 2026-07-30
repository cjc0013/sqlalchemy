# Issue review index

- Frozen upstream base: `aa1a5575358d3aa14953b04dced02f4763fed2e7`
- Catalog release: `20260730.1`
- Outcomes: 79
- Transferable issue outcomes: 51
- Unique transferable units: 50
- Already present: 3
- Validation-only: 21
- No exact transferable unit: 4

- [Unified evidence hub](EVIDENCE_HUB.md)
- [Fork-only maintainer feedback](FEEDBACK.md)

Every issue entry links to its full human-readable packet. Shared units are applied once even when they cover multiple issue outcomes.

## Shared transferable units

### [COLLATION-SCHEMA](review_packets/ISSUE-UNIT-COLLATION-SCHEMA.md)

- Covers issues: #6511, #9693
- Apply once:

```bash
git cherry-pick da97028686f10cbceae7ea1e27480919a7b3287f
```

## Standalone issue patch options (36)

Each row has an isolated commit command.

### Issue #4706 — synonym descriptors automatically blend existing properties - undocumented?

- Review unit: standalone commit [`278cf421a6b18c01ef463e9b97b9cd245082e9de`](review_packets/ISSUE-4706.md)
- Full packet: [`review_packets/ISSUE-4706.md`](review_packets/ISSUE-4706.md)
- Closure mode: `verified_local_option_closure`
- Inspect:

```bash
git show --stat 278cf421a6b18c01ef463e9b97b9cd245082e9de
git show 278cf421a6b18c01ef463e9b97b9cd245082e9de
```

- Apply:

```bash
git cherry-pick 278cf421a6b18c01ef463e9b97b9cd245082e9de
```

### Issue #4790 — Improve error messages on create_table

- Review unit: standalone commit [`70e6b730b53852e27ec5699f6309eba92e820c8c`](review_packets/ISSUE-4790.md)
- Full packet: [`review_packets/ISSUE-4790.md`](review_packets/ISSUE-4790.md)
- Closure mode: `verified_local_option_closure`
- Inspect:

```bash
git show --stat 70e6b730b53852e27ec5699f6309eba92e820c8c
git show 70e6b730b53852e27ec5699f6309eba92e820c8c
```

- Apply:

```bash
git cherry-pick 70e6b730b53852e27ec5699f6309eba92e820c8c
```

### Issue #5005 — alter ORM-level "returned rows" checks to only warn if driver returns -1 or None

- Review unit: standalone commit [`cb16d59854e4fa8bcbbeeed6f4938996c1763481`](review_packets/ISSUE-5005.md)
- Full packet: [`review_packets/ISSUE-5005.md`](review_packets/ISSUE-5005.md)
- Closure mode: `verified_local_option_closure`
- Inspect:

```bash
git show --stat cb16d59854e4fa8bcbbeeed6f4938996c1763481
git show cb16d59854e4fa8bcbbeeed6f4938996c1763481
```

- Apply:

```bash
git cherry-pick cb16d59854e4fa8bcbbeeed6f4938996c1763481
```

### Issue #5350 — `NoReferencedColumnError` when using `referred_column_0[[_]N]_name` in FK naming convention

- Review unit: standalone commit [`908451977266e19296ca8059bf42ce8d50a20f92`](review_packets/ISSUE-5350.md)
- Full packet: [`review_packets/ISSUE-5350.md`](review_packets/ISSUE-5350.md)
- Closure mode: `verified_local_option_closure`
- Inspect:

```bash
git show --stat 908451977266e19296ca8059bf42ce8d50a20f92
git show 908451977266e19296ca8059bf42ce8d50a20f92
```

- Apply:

```bash
git cherry-pick 908451977266e19296ca8059bf42ce8d50a20f92
```

### Issue #6332 — Documentation: use ORM declarative attributes in .values instead of kwargs in "ORM-enabled UPDATE statements"?

- Review unit: standalone commit [`6f8bb8dc84b27dc8bd9e5048de3d1d5152ddb132`](review_packets/ISSUE-6332.md)
- Full packet: [`review_packets/ISSUE-6332.md`](review_packets/ISSUE-6332.md)
- Closure mode: `verified_local_option_closure`
- Inspect:

```bash
git show --stat 6f8bb8dc84b27dc8bd9e5048de3d1d5152ddb132
git show 6f8bb8dc84b27dc8bd9e5048de3d1d5152ddb132
```

- Apply:

```bash
git cherry-pick 6f8bb8dc84b27dc8bd9e5048de3d1d5152ddb132
```

### Issue #6505 — Always include where cluases in delete statements -- at least in test cleanup

- Review unit: standalone commit [`f9cd575cde82631b4c621d46956906f1430a6eb4`](review_packets/ISSUE-6505.md)
- Full packet: [`review_packets/ISSUE-6505.md`](review_packets/ISSUE-6505.md)
- Closure mode: `verified_local_option_closure`
- Inspect:

```bash
git show --stat f9cd575cde82631b4c621d46956906f1430a6eb4
git show f9cd575cde82631b4c621d46956906f1430a6eb4
```

- Apply:

```bash
git cherry-pick f9cd575cde82631b4c621d46956906f1430a6eb4
```

### Issue #6511 — add support for reflection of collation in types (postgresql only, include collate_schema)

- Review unit: [`COLLATION-SCHEMA`](review_packets/ISSUE-UNIT-COLLATION-SCHEMA.md)
- Full packet: [`review_packets/ISSUE-UNIT-COLLATION-SCHEMA.md`](review_packets/ISSUE-UNIT-COLLATION-SCHEMA.md)
- Closure mode: `verified_local_option_closure`
- Inspect:

```bash
git show --stat da97028686f10cbceae7ea1e27480919a7b3287f
git show da97028686f10cbceae7ea1e27480919a7b3287f
```

- Apply: use the shared unit above; do not cherry-pick it twice.

### Issue #6612 — Cannot build SQL expression NOT(x IS NULL) on Postgres

- Review unit: standalone commit [`d5244bbb9527a9161a7fc08cc21d5fb240f1dd42`](review_packets/ISSUE-6612.md)
- Full packet: [`review_packets/ISSUE-6612.md`](review_packets/ISSUE-6612.md)
- Closure mode: `verified_local_option_closure`
- Inspect:

```bash
git show --stat d5244bbb9527a9161a7fc08cc21d5fb240f1dd42
git show d5244bbb9527a9161a7fc08cc21d5fb240f1dd42
```

- Apply:

```bash
git cherry-pick d5244bbb9527a9161a7fc08cc21d5fb240f1dd42
```

### Issue #6860 — smoother with_parent() failure modes

- Review unit: standalone commit [`929a60a51600654eca0b153cc968979f8b24498f`](review_packets/ISSUE-6860.md)
- Full packet: [`review_packets/ISSUE-6860.md`](review_packets/ISSUE-6860.md)
- Closure mode: `verified_local_option_closure`
- Inspect:

```bash
git show --stat 929a60a51600654eca0b153cc968979f8b24498f
git show 929a60a51600654eca0b153cc968979f8b24498f
```

- Apply:

```bash
git cherry-pick 929a60a51600654eca0b153cc968979f8b24498f
```

### Issue #6874 — Please work harder to figure out parameter types for sequences

- Review unit: standalone commit [`27f4a913f99cc99fdf40491746e78d4b71d03d3b`](review_packets/ISSUE-6874.md)
- Full packet: [`review_packets/ISSUE-6874.md`](review_packets/ISSUE-6874.md)
- Closure mode: `verified_local_option_closure`
- Inspect:

```bash
git show --stat 27f4a913f99cc99fdf40491746e78d4b71d03d3b
git show 27f4a913f99cc99fdf40491746e78d4b71d03d3b
```

- Apply:

```bash
git cherry-pick 27f4a913f99cc99fdf40491746e78d4b71d03d3b
```

### Issue #7360 — replace use of the term "primary key identifier" with "identity key" for ORM documentation / methods that refer to the identity map

- Review unit: standalone commit [`2a8d83a114a17208b2430d3f3c4ce39f23338daa`](review_packets/ISSUE-7360.md)
- Full packet: [`review_packets/ISSUE-7360.md`](review_packets/ISSUE-7360.md)
- Closure mode: `verified_local_option_closure`
- Inspect:

```bash
git show --stat 2a8d83a114a17208b2430d3f3c4ce39f23338daa
git show 2a8d83a114a17208b2430d3f3c4ce39f23338daa
```

- Apply:

```bash
git cherry-pick 2a8d83a114a17208b2430d3f3c4ce39f23338daa
```

### Issue #7366 — extend_existing will add copies of indexes, constraints, etc. as there is no deduplication on name

- Review unit: standalone commit [`43136535d03a5f190275ea389cb8c5fe380df672`](review_packets/ISSUE-7366.md)
- Full packet: [`review_packets/ISSUE-7366.md`](review_packets/ISSUE-7366.md)
- Closure mode: `verified_local_option_closure`
- Inspect:

```bash
git show --stat 43136535d03a5f190275ea389cb8c5fe380df672
git show 43136535d03a5f190275ea389cb8c5fe380df672
```

- Apply:

```bash
git cherry-pick 43136535d03a5f190275ea389cb8c5fe380df672
```

### Issue #8805 — Some tests for dialect ignores lack of support of CHECK CONSTRAINT

- Review unit: standalone commit [`8ed8f153ee55da01b8c2667d5b87460bf2b2053f`](review_packets/ISSUE-8805.md)
- Full packet: [`review_packets/ISSUE-8805.md`](review_packets/ISSUE-8805.md)
- Closure mode: `verified_local_option_closure`
- Inspect:

```bash
git show --stat 8ed8f153ee55da01b8c2667d5b87460bf2b2053f
git show 8ed8f153ee55da01b8c2667d5b87460bf2b2053f
```

- Apply:

```bash
git cherry-pick 8ed8f153ee55da01b8c2667d5b87460bf2b2053f
```

### Issue #8894 — Improve documentation to make classes use the "public" module

- Review unit: standalone commit [`09385c459627b0cb24d72e616bb718bd10a57e81`](review_packets/ISSUE-8894.md)
- Full packet: [`review_packets/ISSUE-8894.md`](review_packets/ISSUE-8894.md)
- Closure mode: `verified_local_option_closure`
- Inspect:

```bash
git show --stat 09385c459627b0cb24d72e616bb718bd10a57e81
git show 09385c459627b0cb24d72e616bb718bd10a57e81
```

- Apply:

```bash
git cherry-pick 09385c459627b0cb24d72e616bb718bd10a57e81
```

### Issue #8936 — Make the new PG Range aware of the its bounds data type

- Review unit: standalone commit [`32b7e6e7e186a23923692e53faf9cb1110b620d4`](review_packets/ISSUE-8936.md)
- Full packet: [`review_packets/ISSUE-8936.md`](review_packets/ISSUE-8936.md)
- Closure mode: `verified_local_option_closure`
- Inspect:

```bash
git show --stat 32b7e6e7e186a23923692e53faf9cb1110b620d4
git show 32b7e6e7e186a23923692e53faf9cb1110b620d4
```

- Apply:

```bash
git cherry-pick 32b7e6e7e186a23923692e53faf9cb1110b620d4
```

### Issue #9082 — eager_defaults shouldn't be needed for pk returning even if cols are not actual pks

- Review unit: standalone commit [`019dfdaddee18c126a416ae920debc966400e68b`](review_packets/ISSUE-9082.md)
- Full packet: [`review_packets/ISSUE-9082.md`](review_packets/ISSUE-9082.md)
- Closure mode: `verified_local_option_closure`
- Inspect:

```bash
git show --stat 019dfdaddee18c126a416ae920debc966400e68b
git show 019dfdaddee18c126a416ae920debc966400e68b
```

- Apply:

```bash
git cherry-pick 019dfdaddee18c126a416ae920debc966400e68b
```

### Issue #9212 — add additional type migration section to whatsnew detailing declared_attr format changes, others

- Review unit: standalone commit [`a184b039a48fc3b993346be39277cf58c64ade41`](review_packets/ISSUE-9212.md)
- Full packet: [`review_packets/ISSUE-9212.md`](review_packets/ISSUE-9212.md)
- Closure mode: `verified_local_option_closure`
- Inspect:

```bash
git show --stat a184b039a48fc3b993346be39277cf58c64ade41
git show a184b039a48fc3b993346be39277cf58c64ade41
```

- Apply:

```bash
git cherry-pick a184b039a48fc3b993346be39277cf58c64ade41
```

### Issue #9233 — Expression index does not list all the columns

- Review unit: standalone commit [`c004cf4aabfa967ae4a38f2569b318b0de4923db`](review_packets/ISSUE-9233.md)
- Full packet: [`review_packets/ISSUE-9233.md`](review_packets/ISSUE-9233.md)
- Closure mode: `verified_local_option_closure`
- Inspect:

```bash
git show --stat c004cf4aabfa967ae4a38f2569b318b0de4923db
git show c004cf4aabfa967ae4a38f2569b318b0de4923db
```

- Apply:

```bash
git cherry-pick c004cf4aabfa967ae4a38f2569b318b0de4923db
```

### Issue #9301 — Support mapped attributes that have deferred definitions

- Review unit: standalone commit [`bf08cd63b4401bc315d64a1f05c0b98c4d07ccec`](review_packets/ISSUE-9301.md)
- Full packet: [`review_packets/ISSUE-9301.md`](review_packets/ISSUE-9301.md)
- Closure mode: `verified_local_option_closure`
- Inspect:

```bash
git show --stat bf08cd63b4401bc315d64a1f05c0b98c4d07ccec
git show bf08cd63b4401bc315d64a1f05c0b98c4d07ccec
```

- Apply:

```bash
git cherry-pick bf08cd63b4401bc315d64a1f05c0b98c4d07ccec
```

### Issue #9369 — allow_unmapped seems to not be honored in all cases

- Review unit: standalone commit [`f22279bfce1370cca4801a6b14119ac0833f9a84`](review_packets/ISSUE-9369.md)
- Full packet: [`review_packets/ISSUE-9369.md`](review_packets/ISSUE-9369.md)
- Closure mode: `verified_local_option_closure`
- Inspect:

```bash
git show --stat f22279bfce1370cca4801a6b14119ac0833f9a84
git show f22279bfce1370cca4801a6b14119ac0833f9a84
```

- Apply:

```bash
git cherry-pick f22279bfce1370cca4801a6b14119ac0833f9a84
```

### Issue #9410 — document dataclass gotchas so far

- Review unit: standalone commit [`168923e135fc82b0b5a01b2b91a69725c7b7ecf5`](review_packets/ISSUE-9410.md)
- Full packet: [`review_packets/ISSUE-9410.md`](review_packets/ISSUE-9410.md)
- Closure mode: `verified_local_option_closure`
- Inspect:

```bash
git show --stat 168923e135fc82b0b5a01b2b91a69725c7b7ecf5
git show 168923e135fc82b0b5a01b2b91a69725c7b7ecf5
```

- Apply:

```bash
git cherry-pick 168923e135fc82b0b5a01b2b91a69725c7b7ecf5
```

### Issue #9425 — tighten up compoundselect + textualselect use cases

- Review unit: standalone commit [`82fd41fc014568568babf5b6868d058541173572`](review_packets/ISSUE-9425.md)
- Full packet: [`review_packets/ISSUE-9425.md`](review_packets/ISSUE-9425.md)
- Closure mode: `verified_local_option_closure`
- Inspect:

```bash
git show --stat 82fd41fc014568568babf5b6868d058541173572
git show 82fd41fc014568568babf5b6868d058541173572
```

- Apply:

```bash
git cherry-pick 82fd41fc014568568babf5b6868d058541173572
```

### Issue #9493 — MappedAsDataclass inherits dataclasses attributes, while the spec says they don't

- Review unit: standalone commit [`245794ed686f9e165121f7e53d69fbcd806b2b45`](review_packets/ISSUE-9493.md)
- Full packet: [`review_packets/ISSUE-9493.md`](review_packets/ISSUE-9493.md)
- Closure mode: `verified_local_option_closure`
- Inspect:

```bash
git show --stat 245794ed686f9e165121f7e53d69fbcd806b2b45
git show 245794ed686f9e165121f7e53d69fbcd806b2b45
```

- Apply:

```bash
git cherry-pick 245794ed686f9e165121f7e53d69fbcd806b2b45
```

### Issue #9548 — relationship loader options do a "recursive" thing inconsistently

- Review unit: standalone commit [`626eb012e7adecec2516a20ee8a515b4e1cb6250`](review_packets/ISSUE-9548.md)
- Full packet: [`review_packets/ISSUE-9548.md`](review_packets/ISSUE-9548.md)
- Closure mode: `verified_local_option_closure`
- Inspect:

```bash
git show --stat 626eb012e7adecec2516a20ee8a515b4e1cb6250
git show 626eb012e7adecec2516a20ee8a515b4e1cb6250
```

- Apply:

```bash
git cherry-pick 626eb012e7adecec2516a20ee8a515b4e1cb6250
```

### Issue #9693 — support DDL / SQL time rendering of collation schema across all constructs that include a collation

- Review unit: [`COLLATION-SCHEMA`](review_packets/ISSUE-UNIT-COLLATION-SCHEMA.md)
- Full packet: [`review_packets/ISSUE-UNIT-COLLATION-SCHEMA.md`](review_packets/ISSUE-UNIT-COLLATION-SCHEMA.md)
- Closure mode: `carried_dropped_pr_repair_objective`
- Inspect:

```bash
git show --stat da97028686f10cbceae7ea1e27480919a7b3287f
git show da97028686f10cbceae7ea1e27480919a7b3287f
```

- Apply: use the shared unit above; do not cherry-pick it twice.

### Issue #9944 — Reflect don't recognize foreign tables in postgresql

- Review unit: standalone commit [`483d715186d7a0d176dc749bb358861f6b31d81d`](review_packets/ISSUE-9944.md)
- Full packet: [`review_packets/ISSUE-9944.md`](review_packets/ISSUE-9944.md)
- Closure mode: `verified_local_option_closure`
- Inspect:

```bash
git show --stat 483d715186d7a0d176dc749bb358861f6b31d81d
git show 483d715186d7a0d176dc749bb358861f6b31d81d
```

- Apply:

```bash
git cherry-pick 483d715186d7a0d176dc749bb358861f6b31d81d
```

### Issue #10116 — re-entrant handle_error call if an exception is raised in result.all() within a DML process

- Review unit: standalone commit [`0c2c8eacc041dd069c86806e781a8d198a590b9b`](review_packets/ISSUE-10116.md)
- Full packet: [`review_packets/ISSUE-10116.md`](review_packets/ISSUE-10116.md)
- Closure mode: `verified_local_option_closure`
- Inspect:

```bash
git show --stat 0c2c8eacc041dd069c86806e781a8d198a590b9b
git show 0c2c8eacc041dd069c86806e781a8d198a590b9b
```

- Apply:

```bash
git cherry-pick 0c2c8eacc041dd069c86806e781a8d198a590b9b
```

### Issue #10541 — Improve scalars performance by trying to avoid the creation of a Row

- Review unit: standalone commit [`c6366f7e453e992665a000fba3ab23e5136499e4`](review_packets/ISSUE-10541.md)
- Full packet: [`review_packets/ISSUE-10541.md`](review_packets/ISSUE-10541.md)
- Closure mode: `verified_local_option_closure`
- Inspect:

```bash
git show --stat c6366f7e453e992665a000fba3ab23e5136499e4
git show c6366f7e453e992665a000fba3ab23e5136499e4
```

- Apply:

```bash
git cherry-pick c6366f7e453e992665a000fba3ab23e5136499e4
```

### Issue #10544 — pysqlcipher open fail with err: TypeError: function takes at most 3 arguments (4 given) in dbapi_connection.create_function

- Review unit: standalone commit [`0120e74078d09e0acc868507317045e5a6a51007`](review_packets/ISSUE-10544.md)
- Full packet: [`review_packets/ISSUE-10544.md`](review_packets/ISSUE-10544.md)
- Closure mode: `verified_local_option_closure`
- Inspect:

```bash
git show --stat 0120e74078d09e0acc868507317045e5a6a51007
git show 0120e74078d09e0acc868507317045e5a6a51007
```

- Apply:

```bash
git cherry-pick 0120e74078d09e0acc868507317045e5a6a51007
```

### Issue #10888 — OrderingList typing incorrect / incomplete and implementation doesn't accept non-int indices

- Review unit: standalone commit [`eee3fb2285fda2db38ff88b337d2a53c71f124bd`](review_packets/ISSUE-10888.md)
- Full packet: [`review_packets/ISSUE-10888.md`](review_packets/ISSUE-10888.md)
- Closure mode: `verified_local_option_closure`
- Inspect:

```bash
git show --stat eee3fb2285fda2db38ff88b337d2a53c71f124bd
git show eee3fb2285fda2db38ff88b337d2a53c71f124bd
```

- Apply:

```bash
git cherry-pick eee3fb2285fda2db38ff88b337d2a53c71f124bd
```

### Issue #10960 — "implicit combining column" warning not emitting for two columns from two different aliases against same parent table

- Review unit: standalone commit [`bc15f973a29a80d8f0061105b2a704a5cfbdc482`](review_packets/ISSUE-10960.md)
- Full packet: [`review_packets/ISSUE-10960.md`](review_packets/ISSUE-10960.md)
- Closure mode: `verified_local_option_closure`
- Inspect:

```bash
git show --stat bc15f973a29a80d8f0061105b2a704a5cfbdc482
git show bc15f973a29a80d8f0061105b2a704a5cfbdc482
```

- Apply:

```bash
git cherry-pick bc15f973a29a80d8f0061105b2a704a5cfbdc482
```

### Issue #11062 — Could not de-stringify annotation

- Review unit: standalone commit [`bba9d0fc63e12fd0553d391fec4bd12ae3a74729`](review_packets/ISSUE-11062.md)
- Full packet: [`review_packets/ISSUE-11062.md`](review_packets/ISSUE-11062.md)
- Closure mode: `verified_local_option_closure`
- Inspect:

```bash
git show --stat bba9d0fc63e12fd0553d391fec4bd12ae3a74729
git show bba9d0fc63e12fd0553d391fec4bd12ae3a74729
```

- Apply:

```bash
git cherry-pick bba9d0fc63e12fd0553d391fec4bd12ae3a74729
```

### Issue #11597 — sqltypes.Enum not generic enough

- Review unit: standalone commit [`0d62dfb5241d64999750e68d5896df60e47c490e`](review_packets/ISSUE-11597.md)
- Full packet: [`review_packets/ISSUE-11597.md`](review_packets/ISSUE-11597.md)
- Closure mode: `verified_local_option_closure`
- Inspect:

```bash
git show --stat 0d62dfb5241d64999750e68d5896df60e47c490e
git show 0d62dfb5241d64999750e68d5896df60e47c490e
```

- Apply:

```bash
git cherry-pick 0d62dfb5241d64999750e68d5896df60e47c490e
```

### Issue #12097 — can't adapt type for enum in case()

- Review unit: standalone commit [`ac07c1976b5e3860ff070c078d044995a28c3918`](review_packets/ISSUE-12097.md)
- Full packet: [`review_packets/ISSUE-12097.md`](review_packets/ISSUE-12097.md)
- Closure mode: `verified_local_option_closure`
- Inspect:

```bash
git show --stat ac07c1976b5e3860ff070c078d044995a28c3918
git show ac07c1976b5e3860ff070c078d044995a28c3918
```

- Apply:

```bash
git cherry-pick ac07c1976b5e3860ff070c078d044995a28c3918
```

### Issue #12710 — add extra shielding to async connection create

- Review unit: standalone commit [`d4737a8f08be526d075b4694eb793807fd44b6af`](review_packets/ISSUE-12710.md)
- Full packet: [`review_packets/ISSUE-12710.md`](review_packets/ISSUE-12710.md)
- Closure mode: `verified_local_option_closure`
- Inspect:

```bash
git show --stat d4737a8f08be526d075b4694eb793807fd44b6af
git show d4737a8f08be526d075b4694eb793807fd44b6af
```

- Apply:

```bash
git cherry-pick d4737a8f08be526d075b4694eb793807fd44b6af
```

### Issue #13113 — SQLite insert supports multiple on-conflict clauses in inserts

- Review unit: standalone commit [`3f0fed9f6e49bdbb387566502cddcaf42dc12b56`](review_packets/ISSUE-13113.md)
- Full packet: [`review_packets/ISSUE-13113.md`](review_packets/ISSUE-13113.md)
- Closure mode: `verified_local_option_closure`
- Inspect:

```bash
git show --stat 3f0fed9f6e49bdbb387566502cddcaf42dc12b56
git show 3f0fed9f6e49bdbb387566502cddcaf42dc12b56
```

- Apply:

```bash
git cherry-pick 3f0fed9f6e49bdbb387566502cddcaf42dc12b56
```

## Pull-request-backed issue options (15)

These issues consume the linked PR packet command.

### Issue #4289 — support None for index name

- Review unit: [`PR-13455`](review_packets/PR-13455.md)
- Full packet: [`review_packets/PR-13455.md`](review_packets/PR-13455.md)
- Closure mode: `integrated_current_pr_objective`
- Inspect:

```bash
git show --stat 4e812c2d8440a3946afb90c3c400ff42a7c499c1 fc0941b6887dd549290051450d337565b6744206 9485451520bd75520b82b14d56bac9b33a0dd909 2125396d2fbf150e18b0f05643279f9453ade8e4 95185cb882258bc3c623bfdaa5b9559be1198dc8 045c820e47975ca8e27e0c405978ae1504d13333 82e8ccda1fc4f055845070d8e776e6d702d9a410
git show 4e812c2d8440a3946afb90c3c400ff42a7c499c1 fc0941b6887dd549290051450d337565b6744206 9485451520bd75520b82b14d56bac9b33a0dd909 2125396d2fbf150e18b0f05643279f9453ade8e4 95185cb882258bc3c623bfdaa5b9559be1198dc8 045c820e47975ca8e27e0c405978ae1504d13333 82e8ccda1fc4f055845070d8e776e6d702d9a410
```

- Apply:

```bash
git cherry-pick 4e812c2d8440a3946afb90c3c400ff42a7c499c1 fc0941b6887dd549290051450d337565b6744206 9485451520bd75520b82b14d56bac9b33a0dd909 2125396d2fbf150e18b0f05643279f9453ade8e4 95185cb882258bc3c623bfdaa5b9559be1198dc8 045c820e47975ca8e27e0c405978ae1504d13333 82e8ccda1fc4f055845070d8e776e6d702d9a410
```

### Issue #8992 — tuple expanding params do not render bind_expression() for elements

- Review unit: [`PR-13323`](review_packets/PR-13323.md)
- Full packet: [`review_packets/PR-13323.md`](review_packets/PR-13323.md)
- Closure mode: `integrated_current_pr_objective`
- Inspect:

```bash
git show --stat 32ebdc7a508ea6c32d5152b32bf96451614ccf5d
git show 32ebdc7a508ea6c32d5152b32bf96451614ccf5d
```

- Apply:

```bash
git cherry-pick 32ebdc7a508ea6c32d5152b32bf96451614ccf5d
```

### Issue #9213 — document `@classmethod` add for all `declared_attr` to work w/ typing

- Review unit: [`PR-13436`](review_packets/PR-13436.md)
- Full packet: [`review_packets/PR-13436.md`](review_packets/PR-13436.md)
- Closure mode: `integrated_current_pr_objective`
- Inspect:

```bash
git show --stat 7e8f5cb765c321e50d81f6ecb8b19b5f92546307 37160d9b0f8cedf00514266ce976895c0bf4a2a6 b5a6daa92105c6873b1df7199a18542fc8766568 9a6d0c40ce7c2b1f79be1d06e1a96b870ab9e645
git show 7e8f5cb765c321e50d81f6ecb8b19b5f92546307 37160d9b0f8cedf00514266ce976895c0bf4a2a6 b5a6daa92105c6873b1df7199a18542fc8766568 9a6d0c40ce7c2b1f79be1d06e1a96b870ab9e645
```

- Apply:

```bash
git cherry-pick 7e8f5cb765c321e50d81f6ecb8b19b5f92546307 37160d9b0f8cedf00514266ce976895c0bf4a2a6 b5a6daa92105c6873b1df7199a18542fc8766568 9a6d0c40ce7c2b1f79be1d06e1a96b870ab9e645
```

### Issue #11132 — MySQL DOUBLE accepts deprecated params that dont propagate from the base DOUBLE type, document this caveat

- Review unit: [`PR-13368`](review_packets/PR-13368.md)
- Full packet: [`review_packets/PR-13368.md`](review_packets/PR-13368.md)
- Closure mode: `integrated_current_pr_objective`
- Inspect:

```bash
git show --stat d78abd7a9a169312b344be822152567e429220df
git show d78abd7a9a169312b344be822152567e429220df
```

- Apply:

```bash
git cherry-pick d78abd7a9a169312b344be822152567e429220df
```

### Issue #11620 — Deprecate MSSQL enable_identity_insert by default, gate it behind a flag

- Review unit: [`PR-12297`](review_packets/PR-12297.md)
- Full packet: [`review_packets/PR-12297.md`](review_packets/PR-12297.md)
- Closure mode: `integrated_current_pr_objective`
- Inspect:

```bash
git show --stat ee59fb86d67ed4ecee7abec8b6328ae5ecf172d4
git show ee59fb86d67ed4ecee7abec8b6328ae5ecf172d4
```

- Apply:

```bash
git cherry-pick ee59fb86d67ed4ecee7abec8b6328ae5ecf172d4
```

### Issue #13048 — Add option for disabling automatic addition of constraint/indexes to the table

- Review unit: [`PR-13399`](review_packets/PR-13399.md)
- Full packet: [`review_packets/PR-13399.md`](review_packets/PR-13399.md)
- Closure mode: `integrated_current_pr_objective`
- Inspect:

```bash
git show --stat ec10bde77ab7d062e2c54b67279c7c16836d00a0 b1ac92a48293c27edb0cbb81d05b1a5a053cca7d c81f57b8626485009fdf20c6e983f78f9f0c2a10 b6e57ace6847e3b9c6ebaf3d7ebcf5e37825401e b060340fee665bf8159773b19403fae05dfd45e9
git show ec10bde77ab7d062e2c54b67279c7c16836d00a0 b1ac92a48293c27edb0cbb81d05b1a5a053cca7d c81f57b8626485009fdf20c6e983f78f9f0c2a10 b6e57ace6847e3b9c6ebaf3d7ebcf5e37825401e b060340fee665bf8159773b19403fae05dfd45e9
```

- Apply:

```bash
git cherry-pick ec10bde77ab7d062e2c54b67279c7c16836d00a0 b1ac92a48293c27edb0cbb81d05b1a5a053cca7d c81f57b8626485009fdf20c6e983f78f9f0c2a10 b6e57ace6847e3b9c6ebaf3d7ebcf5e37825401e b060340fee665bf8159773b19403fae05dfd45e9
```

### Issue #13049 — Provide an implementation for avg / abs function with proper type

- Review unit: [`PR-13051`](review_packets/PR-13051.md)
- Full packet: [`review_packets/PR-13051.md`](review_packets/PR-13051.md)
- Closure mode: `integrated_current_pr_objective`
- Inspect:

```bash
git show --stat aa4a415f689599ba872d3c026f94d4f3fb42cbde
git show aa4a415f689599ba872d3c026f94d4f3fb42cbde
```

- Apply:

```bash
git cherry-pick aa4a415f689599ba872d3c026f94d4f3fb42cbde
```

### Issue #13157 — PostgreSQL check constraint reflection strips brackets naively

- Review unit: [`PR-13303`](review_packets/PR-13303.md)
- Full packet: [`review_packets/PR-13303.md`](review_packets/PR-13303.md)
- Closure mode: `integrated_current_pr_objective`
- Inspect:

```bash
git show --stat 8681259072f6727a8c185e2ad0d78924a7ebccbd 7a2c4655c32be43f790187e8289dde06b2de066e 7a4bd805f4033f66602f19db9ea7b7d951639311 caf35a749a29330334adffa8358a46b06e4ed96f 79bb5f3855ab434d9110864bc467bda66de08a2c
git show 8681259072f6727a8c185e2ad0d78924a7ebccbd 7a2c4655c32be43f790187e8289dde06b2de066e 7a4bd805f4033f66602f19db9ea7b7d951639311 caf35a749a29330334adffa8358a46b06e4ed96f 79bb5f3855ab434d9110864bc467bda66de08a2c
```

- Apply:

```bash
git cherry-pick 8681259072f6727a8c185e2ad0d78924a7ebccbd 7a2c4655c32be43f790187e8289dde06b2de066e 7a4bd805f4033f66602f19db9ea7b7d951639311 caf35a749a29330334adffa8358a46b06e4ed96f 79bb5f3855ab434d9110864bc467bda66de08a2c
```

### Issue #13169 — Connection pool soft invalidation uses `time.time()` comparison that can silently fail on low-resolution clocks (e.g. Windows ~16 ms)

- Review unit: [`PR-13288`](review_packets/PR-13288.md)
- Full packet: [`review_packets/PR-13288.md`](review_packets/PR-13288.md)
- Closure mode: `integrated_current_pr_objective`
- Inspect:

```bash
git show --stat 6aac317f3dcf166cc042ed5a085d826b9238da8b
git show 6aac317f3dcf166cc042ed5a085d826b9238da8b
```

- Apply:

```bash
git cherry-pick 6aac317f3dcf166cc042ed5a085d826b9238da8b
```

### Issue #13227 — WriteOnlyMapped: default_factory=list broken in 2.1 due to new declarative_scan validation

- Review unit: [`PR-13289`](review_packets/PR-13289.md)
- Full packet: [`review_packets/PR-13289.md`](review_packets/PR-13289.md)
- Closure mode: `integrated_current_pr_objective`
- Inspect:

```bash
git show --stat 13257b9d85d0748e2a2c6ab44f0717c69cf2d15b 1ff47f96d70078a9e2d2f658e14015e44747542a d645e101e771785d8c93981e2d21148cc559de1e
git show 13257b9d85d0748e2a2c6ab44f0717c69cf2d15b 1ff47f96d70078a9e2d2f658e14015e44747542a d645e101e771785d8c93981e2d21148cc559de1e
```

- Apply:

```bash
git cherry-pick 13257b9d85d0748e2a2c6ab44f0717c69cf2d15b 1ff47f96d70078a9e2d2f658e14015e44747542a d645e101e771785d8c93981e2d21148cc559de1e
```

### Issue #13406 — use new _raw_all_tuples with subqueryloads

- Review unit: [`PR-13404`](review_packets/PR-13404.md)
- Full packet: [`review_packets/PR-13404.md`](review_packets/PR-13404.md)
- Closure mode: `integrated_current_pr_objective`
- Inspect:

```bash
git diff --stat e16498a837a796c9b63ea985ffa56a41307d8725^1 e16498a837a796c9b63ea985ffa56a41307d8725
git diff e16498a837a796c9b63ea985ffa56a41307d8725^1 e16498a837a796c9b63ea985ffa56a41307d8725
```

- Apply:

```bash
git cherry-pick -m 1 e16498a837a796c9b63ea985ffa56a41307d8725
```

### Issue #13407 — Cython batch instance processor — ~10–30% on most loads

- Review unit: [`PR-13405`](review_packets/PR-13405.md)
- Full packet: [`review_packets/PR-13405.md`](review_packets/PR-13405.md)
- Closure mode: `integrated_current_pr_objective`
- Inspect:

```bash
git diff --stat 18dcfb9a2a5f80fe0f640d7c71d19cf8e6020ce4^1 18dcfb9a2a5f80fe0f640d7c71d19cf8e6020ce4
git diff 18dcfb9a2a5f80fe0f640d7c71d19cf8e6020ce4^1 18dcfb9a2a5f80fe0f640d7c71d19cf8e6020ce4
```

- Apply:

```bash
git cherry-pick -m 1 18dcfb9a2a5f80fe0f640d7c71d19cf8e6020ce4
```

### Issue #13433 — Deprecate guess-the-pool in sqlite memory

- Review unit: [`PR-13465`](review_packets/PR-13465.md)
- Full packet: [`review_packets/PR-13465.md`](review_packets/PR-13465.md)
- Closure mode: `integrated_current_pr_objective`
- Inspect:

```bash
git show --stat 0652cc62247eef64d95b1ded25cab707e382aa17 fc50a9837fd50334450ee6c9dd645db1b27b4dad
git show 0652cc62247eef64d95b1ded25cab707e382aa17 fc50a9837fd50334450ee6c9dd645db1b27b4dad
```

- Apply:

```bash
git cherry-pick 0652cc62247eef64d95b1ded25cab707e382aa17 fc50a9837fd50334450ee6c9dd645db1b27b4dad
```

### Issue #13441 — mssql+mssqlpython does not recognize communication failures as disconnects

- Review unit: [`PR-13442`](review_packets/PR-13442.md)
- Full packet: [`review_packets/PR-13442.md`](review_packets/PR-13442.md)
- Closure mode: `integrated_current_pr_objective`
- Inspect:

```bash
git show --stat 3cc7f8f9bae3c588bbf8d2443e69343c6889bc2a f1d6b6a4a82afef454837d5f6081b73085af88aa
git show 3cc7f8f9bae3c588bbf8d2443e69343c6889bc2a f1d6b6a4a82afef454837d5f6081b73085af88aa
```

- Apply:

```bash
git cherry-pick 3cc7f8f9bae3c588bbf8d2443e69343c6889bc2a f1d6b6a4a82afef454837d5f6081b73085af88aa
```

### Issue #13451 — [mssql] reflection sets a spurious length on TEXT/NTEXT columns, yielding invalid TEXT(16) DDL

- Review unit: [`PR-13452`](review_packets/PR-13452.md)
- Full packet: [`review_packets/PR-13452.md`](review_packets/PR-13452.md)
- Closure mode: `integrated_current_pr_objective`
- Inspect:

```bash
git show --stat 87ad77f1a560d08bc2c74a1e141d5388fa464f48 e42e39d67e19206a79c800a5b0fddb9808367b80 7a95286d2c1a18cdadb4efc806c5bbea210e1a06
git show 87ad77f1a560d08bc2c74a1e141d5388fa464f48 e42e39d67e19206a79c800a5b0fddb9808367b80 7a95286d2c1a18cdadb4efc806c5bbea210e1a06
```

- Apply:

```bash
git cherry-pick 87ad77f1a560d08bc2c74a1e141d5388fa464f48 e42e39d67e19206a79c800a5b0fddb9808367b80 7a95286d2c1a18cdadb4efc806c5bbea210e1a06
```

## Already present (3)

The required behavior is already present on the frozen base.

### Issue #6468 — test_limit_render_multiple_times needs order by and seems to be the only union type test.

- Review unit: none
- Full packet: [`review_packets/ISSUE-6468.md`](review_packets/ISSUE-6468.md)
- Closure mode: `verified_upstream_resolved`
- Why no command: the required behavior is already present in the frozen upstream base

### Issue #10742 — Bad PrimaryKeyConstraint metadata for MSSQL temporary table

- Review unit: none
- Full packet: [`review_packets/ISSUE-10742.md`](review_packets/ISSUE-10742.md)
- Closure mode: `verified_upstream_resolved`
- Why no command: the required behavior is already present in the frozen upstream base

### Issue #12341 — Add dialect-specific support for Oracle's FETCH EXACT/APPROXIMATE

- Review unit: none
- Full packet: [`review_packets/ISSUE-12341.md`](review_packets/ISSUE-12341.md)
- Closure mode: `verified_upstream_resolved`
- Why no command: the required behavior is already present in the frozen upstream base

## Validation-only outcomes (21)

These are verified branch-state outcomes, not isolated patch claims.

### Issue #4567 — SQLite on_conflict not working with ORM

- Review unit: none
- Full packet: [`review_packets/ISSUE-4567.md`](review_packets/ISSUE-4567.md)
- Closure mode: `revalidated_acceptance_probe`
- Why no command: the closure is a verified branch-state probe, not an isolated patch

### Issue #4784 — Default MetaData kwarg naming_convention can create issues with certain databases

- Review unit: none
- Full packet: [`review_packets/ISSUE-4784.md`](review_packets/ISSUE-4784.md)
- Closure mode: `revalidated_acceptance_probe`
- Why no command: the closure is a verified branch-state probe, not an isolated patch

### Issue #5139 — Document how to add dialect keywords get_columns() column information

- Review unit: none
- Full packet: [`review_packets/ISSUE-5139.md`](review_packets/ISSUE-5139.md)
- Closure mode: `revalidated_acceptance_probe`
- Why no command: the closure is a verified branch-state probe, not an isolated patch

### Issue #5564 — add limit() / offset() to CTE, as CTE.union() produces a CTE and not a CompoundSelect

- Review unit: none
- Full packet: [`review_packets/ISSUE-5564.md`](review_packets/ISSUE-5564.md)
- Closure mode: `revalidated_acceptance_probe`
- Why no command: the closure is a verified branch-state probe, not an isolated patch

### Issue #5846 — Support reverse bitwise operations

- Review unit: none
- Full packet: [`review_packets/ISSUE-5846.md`](review_packets/ISSUE-5846.md)
- Closure mode: `revalidated_acceptance_probe`
- Why no command: the closure is a verified branch-state probe, not an isolated patch

### Issue #6084 — version_id_col should accept string attr name like polymorphic_on does, make sure all mapper args that point to a column can work like this

- Review unit: none
- Full packet: [`review_packets/ISSUE-6084.md`](review_packets/ISSUE-6084.md)
- Closure mode: `revalidated_acceptance_probe`
- Why no command: the closure is a verified branch-state probe, not an isolated patch

### Issue #7149 — Automap: prefer snake_case over lower() for relationship attribute names

- Review unit: none
- Full packet: [`review_packets/ISSUE-7149.md`](review_packets/ISSUE-7149.md)
- Closure mode: `revalidated_acceptance_probe`
- Why no command: the closure is a verified branch-state probe, not an isolated patch

### Issue #7732 — add new execution option "log_note", implement for ORM queries

- Review unit: none
- Full packet: [`review_packets/ISSUE-7732.md`](review_packets/ISSUE-7732.md)
- Closure mode: `revalidated_acceptance_probe`
- Why no command: the closure is a verified branch-state probe, not an isolated patch

### Issue #8341 — support MySQL 8.0.13's new magical syntax for function server defaults

- Review unit: none
- Full packet: [`review_packets/ISSUE-8341.md`](review_packets/ISSUE-8341.md)
- Closure mode: `revalidated_acceptance_probe`
- Why no command: the closure is a verified branch-state probe, not an isolated patch

### Issue #8693 — sp_reset_connection not called on reused connections in pool. (MSSQL)

- Review unit: none
- Full packet: [`review_packets/ISSUE-8693.md`](review_packets/ISSUE-8693.md)
- Closure mode: `revalidated_acceptance_probe`
- Why no command: the closure is a verified branch-state probe, not an isolated patch

### Issue #9147 — declarative builds permanent strong ref to classes that use declare_first or declare_last

- Review unit: none
- Full packet: [`review_packets/ISSUE-9147.md`](review_packets/ISSUE-9147.md)
- Closure mode: `revalidated_acceptance_probe`
- Why no command: the closure is a verified branch-state probe, not an isolated patch

### Issue #9348 — modify expunge() operation in uow to cascade along delete-orphan in addition to expunge

- Review unit: none
- Full packet: [`review_packets/ISSUE-9348.md`](review_packets/ISSUE-9348.md)
- Closure mode: `revalidated_acceptance_probe`
- Why no command: the closure is a verified branch-state probe, not an isolated patch

### Issue #9839 — document network-related caveats for insertmanyvalues

- Review unit: none
- Full packet: [`review_packets/ISSUE-9839.md`](review_packets/ISSUE-9839.md)
- Closure mode: `revalidated_acceptance_probe`
- Why no command: the closure is a verified branch-state probe, not an isolated patch

### Issue #9930 — need docs /warnings that `__init__` is not called on load

- Review unit: none
- Full packet: [`review_packets/ISSUE-9930.md`](review_packets/ISSUE-9930.md)
- Closure mode: `revalidated_acceptance_probe`
- Why no command: the closure is a verified branch-state probe, not an isolated patch

### Issue #10094 — document asyncio gotchas so far

- Review unit: none
- Full packet: [`review_packets/ISSUE-10094.md`](review_packets/ISSUE-10094.md)
- Closure mode: `revalidated_acceptance_probe`
- Why no command: the closure is a verified branch-state probe, not an isolated patch

### Issue #10380 — Declaring Composite Column Types as Optional leads to NULL data type for constituent columns in table definition

- Review unit: none
- Full packet: [`review_packets/ISSUE-10380.md`](review_packets/ISSUE-10380.md)
- Closure mode: `revalidated_acceptance_probe`
- Why no command: the closure is a verified branch-state probe, not an isolated patch

### Issue #10527 — Wrong typing for `with_for_update()`'s `of` argument.

- Review unit: none
- Full packet: [`review_packets/ISSUE-10527.md`](review_packets/ISSUE-10527.md)
- Closure mode: `revalidated_acceptance_probe`
- Why no command: the closure is a verified branch-state probe, not an isolated patch

### Issue #11284 — Missing batch_op.f()

- Review unit: none
- Full packet: [`review_packets/ISSUE-11284.md`](review_packets/ISSUE-11284.md)
- Closure mode: `revalidated_acceptance_probe`
- Why no command: the closure is a verified branch-state probe, not an isolated patch

### Issue #12561 — Recover two-phase in mysql is currently unusable since it uses a legacy row index method

- Review unit: none
- Full packet: [`review_packets/ISSUE-12561.md`](review_packets/ISSUE-12561.md)
- Closure mode: `revalidated_acceptance_probe`
- Why no command: the closure is a verified branch-state probe, not an isolated patch

### Issue #13204 — Immediateload fails to load when combined with inheritance

- Review unit: none
- Full packet: [`review_packets/ISSUE-13204.md`](review_packets/ISSUE-13204.md)
- Closure mode: `revalidated_acceptance_probe`
- Why no command: the closure is a verified branch-state probe, not an isolated patch

### Issue #13210 — Applying a loader option to a parent relationship when using with_polymorphic does not work properly

- Review unit: none
- Full packet: [`review_packets/ISSUE-13210.md`](review_packets/ISSUE-13210.md)
- Closure mode: `revalidated_acceptance_probe`
- Why no command: the closure is a verified branch-state probe, not an isolated patch

## No exact unit asserted (4)

The frozen evidence does not justify an isolated command.

### Issue #5123 — apply informative re-raise if a result processor function fails

- Review unit: none
- Full packet: [`review_packets/ISSUE-5123.md`](review_packets/ISSUE-5123.md)
- Closure mode: `verified_local_option_closure`
- Why no command: the available commit series does not apply cleanly from the frozen upstream base, so no standalone apply command is asserted

### Issue #7517 — Better document `expanding=True` on a bind parameter

- Review unit: none
- Full packet: [`review_packets/ISSUE-7517.md`](review_packets/ISSUE-7517.md)
- Closure mode: `verified_local_option_closure`
- Why no command: the available commit series does not apply cleanly from the frozen upstream base, so no standalone apply command is asserted

### Issue #10835 — sqlalchemy.util.OrderedSet does not work with v2 in ORM mappings

- Review unit: none
- Full packet: [`review_packets/ISSUE-10835.md`](review_packets/ISSUE-10835.md)
- Closure mode: `verified_local_option_closure`
- Why no command: the available commit series does not apply cleanly from the frozen upstream base, so no standalone apply command is asserted

### Issue #11677 — SQLITE: SQLiteDialect.get_check_constraints incorrectly reflects multiline check constraints

- Review unit: none
- Full packet: [`review_packets/ISSUE-11677.md`](review_packets/ISSUE-11677.md)
- Closure mode: `verified_local_option_closure`
- Why no command: no standalone technical unit is asserted by the frozen evidence
