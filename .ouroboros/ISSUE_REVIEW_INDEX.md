# Issue review index

All 80 locally classified issue outcomes are listed here. Commands are copied from the machine-readable issue catalog.

## Standalone issue patch options (40)

Each row has an isolated commit command.

### Issue #4706 — synonym descriptors automatically blend existing properties - undocumented?

- Review unit: none
- Closure mode: `verified_local_option_closure`
- Apply:

```bash
git cherry-pick 278cf421a6b18c01ef463e9b97b9cd245082e9de
```

### Issue #4790 — Improve error messages on create_table

- Review unit: none
- Closure mode: `verified_local_option_closure`
- Apply:

```bash
git cherry-pick 70e6b730b53852e27ec5699f6309eba92e820c8c
```

### Issue #5005 — alter ORM-level "returned rows" checks to only warn if driver returns -1 or None

- Review unit: none
- Closure mode: `verified_local_option_closure`
- Apply:

```bash
git cherry-pick cb16d59854e4fa8bcbbeeed6f4938996c1763481
```

### Issue #5123 — apply informative re-raise if a result processor function fails

- Review unit: none
- Closure mode: `verified_local_option_closure`
- Apply:

```bash
git cherry-pick 86bec267f7041e312c1a100b9296edbf30a8a63a
```

### Issue #5350 — `NoReferencedColumnError` when using `referred_column_0[[_]N]_name` in FK naming convention

- Review unit: none
- Closure mode: `verified_local_option_closure`
- Apply:

```bash
git cherry-pick 908451977266e19296ca8059bf42ce8d50a20f92
```

### Issue #6332 — Documentation: use ORM declarative attributes in .values instead of kwargs in "ORM-enabled UPDATE statements"?

- Review unit: none
- Closure mode: `verified_local_option_closure`
- Apply:

```bash
git cherry-pick 6f8bb8dc84b27dc8bd9e5048de3d1d5152ddb132
```

### Issue #6505 — Always include where cluases in delete statements -- at least in test cleanup

- Review unit: none
- Closure mode: `verified_local_option_closure`
- Apply:

```bash
git cherry-pick f9cd575cde82631b4c621d46956906f1430a6eb4
```

### Issue #6511 — add support for reflection of collation in types (postgresql only, include collate_schema)

- Review unit: none
- Closure mode: `verified_local_option_closure`
- Apply:

```bash
git cherry-pick da97028686f10cbceae7ea1e27480919a7b3287f
```

### Issue #6612 — Cannot build SQL expression NOT(x IS NULL) on Postgres

- Review unit: none
- Closure mode: `verified_local_option_closure`
- Apply:

```bash
git cherry-pick d5244bbb9527a9161a7fc08cc21d5fb240f1dd42
```

### Issue #6860 — smoother with_parent() failure modes

- Review unit: none
- Closure mode: `verified_local_option_closure`
- Apply:

```bash
git cherry-pick 929a60a51600654eca0b153cc968979f8b24498f
```

### Issue #6874 — Please work harder to figure out parameter types for sequences

- Review unit: none
- Closure mode: `verified_local_option_closure`
- Apply:

```bash
git cherry-pick 27f4a913f99cc99fdf40491746e78d4b71d03d3b
```

### Issue #7360 — replace use of the term "primary key identifier" with "identity key" for ORM documentation / methods that refer to the identity map

- Review unit: none
- Closure mode: `verified_local_option_closure`
- Apply:

```bash
git cherry-pick 2a8d83a114a17208b2430d3f3c4ce39f23338daa
```

### Issue #7366 — extend_existing will add copies of indexes, constraints, etc. as there is no deduplication on name

- Review unit: none
- Closure mode: `verified_local_option_closure`
- Apply:

```bash
git cherry-pick 43136535d03a5f190275ea389cb8c5fe380df672
```

### Issue #7517 — Better document `expanding=True` on a bind parameter

- Review unit: none
- Closure mode: `verified_local_option_closure`
- Apply:

```bash
git cherry-pick f0f5ef3fb50b1b24d9fee23635f4b3adf0726a91 77d27749ea50b5a5a86b10d01b2449765578eb0f
```

### Issue #8805 — Some tests for dialect ignores lack of support of CHECK CONSTRAINT

- Review unit: none
- Closure mode: `verified_local_option_closure`
- Apply:

```bash
git cherry-pick 8ed8f153ee55da01b8c2667d5b87460bf2b2053f
```

### Issue #8894 — Improve documentation to make classes use the "public" module

- Review unit: none
- Closure mode: `verified_local_option_closure`
- Apply:

```bash
git cherry-pick 09385c459627b0cb24d72e616bb718bd10a57e81
```

### Issue #8936 — Make the new PG Range aware of the its bounds data type

- Review unit: none
- Closure mode: `verified_local_option_closure`
- Apply:

```bash
git cherry-pick 32b7e6e7e186a23923692e53faf9cb1110b620d4
```

### Issue #9082 — eager_defaults shouldn't be needed for pk returning even if cols are not actual pks

- Review unit: none
- Closure mode: `verified_local_option_closure`
- Apply:

```bash
git cherry-pick 019dfdaddee18c126a416ae920debc966400e68b
```

### Issue #9212 — add additional type migration section to whatsnew detailing declared_attr format changes, others

- Review unit: none
- Closure mode: `verified_local_option_closure`
- Apply:

```bash
git cherry-pick a184b039a48fc3b993346be39277cf58c64ade41
```

### Issue #9233 — Expression index does not list all the columns

- Review unit: none
- Closure mode: `verified_local_option_closure`
- Apply:

```bash
git cherry-pick c004cf4aabfa967ae4a38f2569b318b0de4923db
```

### Issue #9301 — Support mapped attributes that have deferred definitions

- Review unit: none
- Closure mode: `verified_local_option_closure`
- Apply:

```bash
git cherry-pick bf08cd63b4401bc315d64a1f05c0b98c4d07ccec
```

### Issue #9369 — allow_unmapped seems to not be honored in all cases

- Review unit: none
- Closure mode: `verified_local_option_closure`
- Apply:

```bash
git cherry-pick f22279bfce1370cca4801a6b14119ac0833f9a84
```

### Issue #9410 — document dataclass gotchas so far

- Review unit: none
- Closure mode: `verified_local_option_closure`
- Apply:

```bash
git cherry-pick 168923e135fc82b0b5a01b2b91a69725c7b7ecf5
```

### Issue #9425 — tighten up compoundselect + textualselect use cases

- Review unit: none
- Closure mode: `verified_local_option_closure`
- Apply:

```bash
git cherry-pick 82fd41fc014568568babf5b6868d058541173572
```

### Issue #9493 — MappedAsDataclass inherits dataclasses attributes, while the spec says they don't

- Review unit: none
- Closure mode: `verified_local_option_closure`
- Apply:

```bash
git cherry-pick 245794ed686f9e165121f7e53d69fbcd806b2b45
```

### Issue #9548 — relationship loader options do a "recursive" thing inconsistently

- Review unit: none
- Closure mode: `verified_local_option_closure`
- Apply:

```bash
git cherry-pick 626eb012e7adecec2516a20ee8a515b4e1cb6250
```

### Issue #9693 — support DDL / SQL time rendering of collation schema across all constructs that include a collation

- Review unit: none
- Closure mode: `carried_dropped_pr_repair_objective`
- Apply:

```bash
git cherry-pick da97028686f10cbceae7ea1e27480919a7b3287f
```

### Issue #9944 — Reflect don't recognize foreign tables in postgresql

- Review unit: none
- Closure mode: `verified_local_option_closure`
- Apply:

```bash
git cherry-pick 483d715186d7a0d176dc749bb358861f6b31d81d
```

### Issue #10116 — re-entrant handle_error call if an exception is raised in result.all() within a DML process

- Review unit: none
- Closure mode: `verified_local_option_closure`
- Apply:

```bash
git cherry-pick 0c2c8eacc041dd069c86806e781a8d198a590b9b
```

### Issue #10541 — Improve scalars performance by trying to avoid the creation of a Row

- Review unit: none
- Closure mode: `verified_local_option_closure`
- Apply:

```bash
git cherry-pick c6366f7e453e992665a000fba3ab23e5136499e4
```

### Issue #10544 — pysqlcipher open fail with err: TypeError: function takes at most 3 arguments (4 given) in dbapi_connection.create_function

- Review unit: none
- Closure mode: `verified_local_option_closure`
- Apply:

```bash
git cherry-pick 0120e74078d09e0acc868507317045e5a6a51007
```

### Issue #10835 — sqlalchemy.util.OrderedSet does not work with v2 in ORM mappings

- Review unit: none
- Closure mode: `verified_local_option_closure`
- Apply:

```bash
git cherry-pick 368c7076a4005e0abbb2392c56e1a851f8b7f20f
```

### Issue #10888 — OrderingList typing incorrect / incomplete and implementation doesn't accept non-int indices

- Review unit: none
- Closure mode: `verified_local_option_closure`
- Apply:

```bash
git cherry-pick eee3fb2285fda2db38ff88b337d2a53c71f124bd
```

### Issue #10960 — "implicit combining column" warning not emitting for two columns from two different aliases against same parent table

- Review unit: none
- Closure mode: `verified_local_option_closure`
- Apply:

```bash
git cherry-pick bc15f973a29a80d8f0061105b2a704a5cfbdc482
```

### Issue #11062 — Could not de-stringify annotation

- Review unit: none
- Closure mode: `verified_local_option_closure`
- Apply:

```bash
git cherry-pick bba9d0fc63e12fd0553d391fec4bd12ae3a74729
```

### Issue #11597 — sqltypes.Enum not generic enough

- Review unit: none
- Closure mode: `verified_local_option_closure`
- Apply:

```bash
git cherry-pick 0d62dfb5241d64999750e68d5896df60e47c490e
```

### Issue #11677 — SQLITE: SQLiteDialect.get_check_constraints incorrectly reflects multiline check constraints

- Review unit: none
- Closure mode: `verified_local_option_closure`
- Apply:

```bash
git cherry-pick 600851433f2bb7c940d6ad62e14dc5803698ac7b
```

### Issue #12097 — can't adapt type for enum in case()

- Review unit: none
- Closure mode: `verified_local_option_closure`
- Apply:

```bash
git cherry-pick ac07c1976b5e3860ff070c078d044995a28c3918
```

### Issue #12710 — add extra shielding to async connection create

- Review unit: none
- Closure mode: `verified_local_option_closure`
- Apply:

```bash
git cherry-pick d4737a8f08be526d075b4694eb793807fd44b6af
```

### Issue #13113 — SQLite insert supports multiple on-conflict clauses in inserts

- Review unit: none
- Closure mode: `verified_local_option_closure`
- Apply:

```bash
git cherry-pick 3f0fed9f6e49bdbb387566502cddcaf42dc12b56
```

## Pull-request-backed issue options (16)

These issues consume the linked PR packet command.

### Issue #4289 — support None for index name

- Review unit: PR-13455
- Closure mode: `integrated_current_pr_objective`
- Apply:

```bash
git cherry-pick 66c529e6f5b007fc6c2577641e927d97709177f5 ed7176e271c48981c9f214f1afee91ac65e50df3 730dccdb2f90d0aa629b5c53ffe963a656b6abb8 dfb3f4ec31aadd08bf666898bc0286c4793d5f1e 508281ec8b3b1bba33f8cc1c4dc35b9ad512f445 ba50f18f9cb6e77989ec867ce4ec60a5d6e142d4 aeb0d4a01f6d602ed559c4a367e52a7288ff54d1
```

### Issue #8992 — tuple expanding params do not render bind_expression() for elements

- Review unit: PR-13323
- Closure mode: `integrated_current_pr_objective`
- Apply:

```bash
git cherry-pick 3a2ad769e54486fce8ae0229904932a59422f5df
```

### Issue #9213 — document `@classmethod` add for all `declared_attr` to work w/ typing

- Review unit: PR-13436
- Closure mode: `integrated_current_pr_objective`
- Apply:

```bash
git cherry-pick b9bcad398bcec0172d6a587f0c585498f14efd54 68897644127ab814809d73214c9501c6c644b669 31312d602da0d3a2b2e1a696805a9c6c8e3d0f99 fbed8e7ae20afc41f89f6f557d92120479a5c8e5
```

### Issue #10675 — syntax error with mysql bulk update via INSERT ... SELECT ... ON DUPLICATE KEY UPDATE

- Review unit: PR-13454
- Closure mode: `integrated_current_pr_objective`
- Apply:

```bash
git cherry-pick c683e3990b8a39bb6636d3994138aef6c9aa0435
```

### Issue #11132 — MySQL DOUBLE accepts deprecated params that dont propagate from the base DOUBLE type, document this caveat

- Review unit: PR-13368
- Closure mode: `integrated_current_pr_objective`
- Apply:

```bash
git cherry-pick 46eba5f3a6e0245fbd727d6a06e9954b0fa53317
```

### Issue #11620 — Deprecate MSSQL enable_identity_insert by default, gate it behind a flag

- Review unit: PR-12297
- Closure mode: `integrated_current_pr_objective`
- Apply:

```bash
git cherry-pick ee59fb86d67ed4ecee7abec8b6328ae5ecf172d4
```

### Issue #13048 — Add option for disabling automatic addition of constraint/indexes to the table

- Review unit: PR-13399
- Closure mode: `integrated_current_pr_objective`
- Apply:

```bash
git cherry-pick 803936d6dbdc5c32bf9f8583c89242a8821cf549 315e3d475255761c4b1094f6e434f82c4c38512f ea620f8c0f3a00ec9df247548b543c526a616d0d 1cf88365165d2b415adcb58016f334e313e8f04a b6a7da10e1144ffa6d75b6845f49d3aeddbb3837
```

### Issue #13049 — Provide an implementation for avg / abs function with proper type

- Review unit: PR-13051
- Closure mode: `integrated_current_pr_objective`
- Apply:

```bash
git cherry-pick aa4a415f689599ba872d3c026f94d4f3fb42cbde
```

### Issue #13157 — PostgreSQL check constraint reflection strips brackets naively

- Review unit: PR-13303
- Closure mode: `integrated_current_pr_objective`
- Apply:

```bash
git cherry-pick f123dac425868ae9451d22c809e100797276fa78 600851433f2bb7c940d6ad62e14dc5803698ac7b 6a61ed52aacd28a9ad96155ec785408262c9d748 ba644bdba114e2c74788d6af66fd29327f609976 7d839925d0132a801f2822c02a95cd34929da1a7
```

### Issue #13169 — Connection pool soft invalidation uses `time.time()` comparison that can silently fail on low-resolution clocks (e.g. Windows ~16 ms)

- Review unit: PR-13288
- Closure mode: `integrated_current_pr_objective`
- Apply:

```bash
git cherry-pick 91feee81b9b077bf41f47b8f757120e293f767f6
```

### Issue #13227 — WriteOnlyMapped: default_factory=list broken in 2.1 due to new declarative_scan validation

- Review unit: PR-13289
- Closure mode: `integrated_current_pr_objective`
- Apply:

```bash
git cherry-pick b723c4396d31fa1daca7028125bd1a4a523ea1bc f6eb1429a6bc7b38d0928c1b4b79d0c34e3f8f18 90f8d18ce7af306d5ee23af4c0ac9c5bcc13975f
```

### Issue #13357 — Type check error when passing lists to `any_`/`all_`

- Review unit: PR-13456
- Closure mode: `integrated_current_pr_objective`
- Apply:

```bash
git cherry-pick f7ee08dff52e11ff116330ee30ac6c0fccd4e88d
```

### Issue #13406 — use new _raw_all_tuples with subqueryloads

- Review unit: PR-13404
- Closure mode: `integrated_current_pr_objective`
- Apply:

```bash
git cherry-pick -m 1 e16498a837a796c9b63ea985ffa56a41307d8725
```

### Issue #13407 — Cython batch instance processor — ~10–30% on most loads

- Review unit: PR-13405
- Closure mode: `integrated_current_pr_objective`
- Apply:

```bash
git cherry-pick -m 1 18dcfb9a2a5f80fe0f640d7c71d19cf8e6020ce4
```

### Issue #13441 — mssql+mssqlpython does not recognize communication failures as disconnects

- Review unit: PR-13442
- Closure mode: `integrated_current_pr_objective`
- Apply:

```bash
git cherry-pick 009aa8de09dd28370a1671f3d23a4b118e76b4b1 275db93c787cf64163d922d545d52054bc4e6c17
```

### Issue #13451 — [mssql] reflection sets a spurious length on TEXT/NTEXT columns, yielding invalid TEXT(16) DDL

- Review unit: PR-13452
- Closure mode: `integrated_current_pr_objective`
- Apply:

```bash
git cherry-pick dffe45ac22539cc70f2307133829f4a63ce07ff1 d5b1fb13635a3c4534faeaf335b59c0833b2b686 d1ecaa664201282920618461bc4383cb51bc64f4
```

## Already present (3)

The required behavior is already present on the frozen base.

### Issue #6468 — test_limit_render_multiple_times needs order by and seems to be the only union type test.

- Review unit: none
- Closure mode: `verified_upstream_resolved`
- Why no command: the required behavior is already present in the frozen upstream base

### Issue #10742 — Bad PrimaryKeyConstraint metadata for MSSQL temporary table

- Review unit: none
- Closure mode: `verified_upstream_resolved`
- Why no command: the required behavior is already present in the frozen upstream base

### Issue #12341 — Add dialect-specific support for Oracle's FETCH EXACT/APPROXIMATE

- Review unit: none
- Closure mode: `verified_upstream_resolved`
- Why no command: the required behavior is already present in the frozen upstream base

## Validation-only outcomes (21)

These are verified branch-state outcomes, not isolated patch claims.

### Issue #4567 — SQLite on_conflict not working with ORM

- Review unit: none
- Closure mode: `revalidated_acceptance_probe`
- Why no command: the closure is a verified branch-state probe, not an isolated patch

### Issue #4784 — Default MetaData kwarg naming_convention can create issues with certain databases

- Review unit: none
- Closure mode: `revalidated_acceptance_probe`
- Why no command: the closure is a verified branch-state probe, not an isolated patch

### Issue #5139 — Document how to add dialect keywords get_columns() column information

- Review unit: none
- Closure mode: `revalidated_acceptance_probe`
- Why no command: the closure is a verified branch-state probe, not an isolated patch

### Issue #5564 — add limit() / offset() to CTE, as CTE.union() produces a CTE and not a CompoundSelect

- Review unit: none
- Closure mode: `revalidated_acceptance_probe`
- Why no command: the closure is a verified branch-state probe, not an isolated patch

### Issue #5846 — Support reverse bitwise operations

- Review unit: none
- Closure mode: `revalidated_acceptance_probe`
- Why no command: the closure is a verified branch-state probe, not an isolated patch

### Issue #6084 — version_id_col should accept string attr name like polymorphic_on does, make sure all mapper args that point to a column can work like this

- Review unit: none
- Closure mode: `revalidated_acceptance_probe`
- Why no command: the closure is a verified branch-state probe, not an isolated patch

### Issue #7149 — Automap: prefer snake_case over lower() for relationship attribute names

- Review unit: none
- Closure mode: `revalidated_acceptance_probe`
- Why no command: the closure is a verified branch-state probe, not an isolated patch

### Issue #7732 — add new execution option "log_note", implement for ORM queries

- Review unit: none
- Closure mode: `revalidated_acceptance_probe`
- Why no command: the closure is a verified branch-state probe, not an isolated patch

### Issue #8341 — support MySQL 8.0.13's new magical syntax for function server defaults

- Review unit: none
- Closure mode: `revalidated_acceptance_probe`
- Why no command: the closure is a verified branch-state probe, not an isolated patch

### Issue #8693 — sp_reset_connection not called on reused connections in pool. (MSSQL)

- Review unit: none
- Closure mode: `revalidated_acceptance_probe`
- Why no command: the closure is a verified branch-state probe, not an isolated patch

### Issue #9147 — declarative builds permanent strong ref to classes that use declare_first or declare_last

- Review unit: none
- Closure mode: `revalidated_acceptance_probe`
- Why no command: the closure is a verified branch-state probe, not an isolated patch

### Issue #9348 — modify expunge() operation in uow to cascade along delete-orphan in addition to expunge

- Review unit: none
- Closure mode: `revalidated_acceptance_probe`
- Why no command: the closure is a verified branch-state probe, not an isolated patch

### Issue #9839 — document network-related caveats for insertmanyvalues

- Review unit: none
- Closure mode: `revalidated_acceptance_probe`
- Why no command: the closure is a verified branch-state probe, not an isolated patch

### Issue #9930 — need docs /warnings that `__init__` is not called on load

- Review unit: none
- Closure mode: `revalidated_acceptance_probe`
- Why no command: the closure is a verified branch-state probe, not an isolated patch

### Issue #10094 — document asyncio gotchas so far

- Review unit: none
- Closure mode: `revalidated_acceptance_probe`
- Why no command: the closure is a verified branch-state probe, not an isolated patch

### Issue #10380 — Declaring Composite Column Types as Optional leads to NULL data type for constituent columns in table definition

- Review unit: none
- Closure mode: `revalidated_acceptance_probe`
- Why no command: the closure is a verified branch-state probe, not an isolated patch

### Issue #10527 — Wrong typing for `with_for_update()`'s `of` argument.

- Review unit: none
- Closure mode: `revalidated_acceptance_probe`
- Why no command: the closure is a verified branch-state probe, not an isolated patch

### Issue #11284 — Missing batch_op.f()

- Review unit: none
- Closure mode: `revalidated_acceptance_probe`
- Why no command: the closure is a verified branch-state probe, not an isolated patch

### Issue #12561 — Recover two-phase in mysql is currently unusable since it uses a legacy row index method

- Review unit: none
- Closure mode: `revalidated_acceptance_probe`
- Why no command: the closure is a verified branch-state probe, not an isolated patch

### Issue #13204 — Immediateload fails to load when combined with inheritance

- Review unit: none
- Closure mode: `revalidated_acceptance_probe`
- Why no command: the closure is a verified branch-state probe, not an isolated patch

### Issue #13210 — Applying a loader option to a parent relationship when using with_polymorphic does not work properly

- Review unit: none
- Closure mode: `revalidated_acceptance_probe`
- Why no command: the closure is a verified branch-state probe, not an isolated patch

## No exact unit asserted (0)

The frozen evidence does not justify an isolated command.

None.
