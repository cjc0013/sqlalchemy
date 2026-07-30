# Unified maintainer evidence hub

## What this is

This is a catalog of possible SQLAlchemy fixes intended to reduce maintainer
workload. It makes alternatives easy to inspect, test, cherry-pick, revise, or
decline. A packet is evidence and an implementation possibility, not a claim
that the change is perfect, accepted upstream, or ready to merge unchanged.

## Current option: issue 13447

The newest option addresses **PostgreSQL schema-qualified collation support**
against a current upstream base. It is intentionally separate from the older
frozen catalog counts.

- [Human review packet](https://github.com/cjc0013/sqlalchemy/blob/ouroboros/issue-13447-review-20260730/.ouroboros/ISSUE-13447.md)
- [Clean code branch](https://github.com/cjc0013/sqlalchemy/tree/ouroboros/issue-13447-20260730)
- Base: `d9b44cb731bd27e6e82c99a3c0fb598214e8e7ff`
- Code head: `9eb6026dad03a987f891af03395f6eb49260edbd`
- Apply: `git cherry-pick 7836a24696b6592594827f7f23391af4eb39c163 cb0d965aa39a1cfb23c730b985c96c091f40d690 9eb6026dad03a987f891af03395f6eb49260edbd`

## Pick a possible fix

- [Pull-request review queue](MAINTAINER_REVIEW_INDEX.md)
- [Issue review index](ISSUE_REVIEW_INDEX.md)
- [All detailed packets](review_packets/)
- [Selective consumption guide](REVIEW_GUIDE.md)

The frozen snapshot contains 24 pull-request
packets and 79 issue outcomes. Of those issue outcomes,
51 have commands representing
50 unique transferable units.

## Unified evidence

- Non-typing suite: 25800 passed, 1502 skipped,
  0 failed, 0 errors.
- Typing suite: 77 passed; its recorded failure boundary matches
  the frozen upstream baseline.
- Focused receipts, CI attribution, coverage, commit order, packet routing, and
  publication hashes are joined in [`evidence_bundle.json`](evidence_bundle.json).
- [`publication_manifest.json`](publication_manifest.json) hashes every published
  artifact.

## Feedback and lifecycle

No maintainer interaction is required. Without feedback, this release remains a
static, usable snapshot and every exact commit stays cherry-pickable.

If a maintainer asks why something was done, requests a different shape, prefers
one option, or rejects an approach, that feedback can drive a new release while
the previous evidence remains intact.

- [Open a fork-only feedback issue](https://github.com/cjc0013/sqlalchemy/issues/new?title=Option+feedback%3A+%3Creview+unit%3E&body=Review+unit%3A+%3Cpacket+ID%2C+issue+number%2C+or+commit%3E%0ACommit%3A+%3Ccommit+SHA+or+unknown%3E%0ADisposition%3A+question%0AFeedback%3A+%3Cwhat+should+change%2C+or+what+needs+explanation%3E%0AFile+or+symbol%3A+%3Coptional%3E%0ASuggested+change%3A+%3Coptional%3E%0A&labels=ouroboros-feedback)
- [Read the feedback guide](FEEDBACK.md)
- Machine contract: [`feedback_contract.json`](feedback_contract.json)

## Evidence shape

`README.md` points here. This hub points to the human queues. Each queue points to
a packet. Each packet points to an exact commit series and its validation. The
machine bundle mirrors those links so Ouroboros can rehydrate the whole catalog
without scraping prose.
