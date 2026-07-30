# Maintainer feedback

Feedback is welcome but not required. The catalog is useful as a static set of
cherry-pickable possibilities when nobody responds. When feedback arrives, it
becomes input to the next catalog release; previous commits and receipts remain
available rather than being silently rewritten.

## Fastest path

[Open a fork-only feedback issue](https://github.com/cjc0013/sqlalchemy/issues/new?title=Option+feedback%3A+%3Creview+unit%3E&body=Review+unit%3A+%3Cpacket+ID%2C+issue+number%2C+or+commit%3E%0ACommit%3A+%3Ccommit+SHA+or+unknown%3E%0ADisposition%3A+question%0AFeedback%3A+%3Cwhat+should+change%2C+or+what+needs+explanation%3E%0AFile+or+symbol%3A+%3Coptional%3E%0ASuggested+change%3A+%3Coptional%3E%0A&labels=ouroboros-feedback). This creates an issue on
`cjc0013/sqlalchemy`, not on the upstream SQLAlchemy repository.

Only two things are required:

1. The review unit, issue number, or commit you mean.
2. The question, requested change, preference, or reason to decline it.

Natural language is enough. File names, symbols, tests, and a proposed direction
are optional. Useful dispositions are `question`, `revise`, `prefer`,
`accept-as-option`, `decline`, and `blocked`.

## What happens next

Ouroboros normalizes labeled fork feedback into `sqlalchemy_option_feedback_v1`,
deduplicates it by issue and update time, associates it with the review unit and
commit, and marks the option for explanation, revision, replacement, or no
change. No maintainer behavior model is published or required.

The machine contract is `feedback_contract.json`. Feedback can also be relayed
through another channel using the same field names; opening a fork issue is
simply the easiest public route.
