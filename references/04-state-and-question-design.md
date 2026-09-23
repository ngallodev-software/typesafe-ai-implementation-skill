# State and question design

**Classification:** PUBLIC-DERIVED / PROJECT-GUIDANCE

## State is evidence

The question should be answerable from the state supplied. Include identities,
relationships, policy facts, source evidence, and candidate definitions that materially
affect the judgment.

Prefer:

```json
{
  "requirement": {"id": "REQ-7", "text": "..."},
  "preservation": [{"id": "P-2", "text": "..."}],
  "repository_evidence": [
    {"id": "E-4", "path": "src/auth.py", "fact": "..."}
  ]
}
```

over an unlabeled concatenated prompt blob.

## Preserve epistemic categories

Keep these distinct when they exist:

- observed source facts;
- deterministic derived facts;
- prior semantic/model inferences;
- user-authorized decisions;
- current policy/constraints.

A model should not mistake a prior inference for source truth simply because both are in
one text field.

## Question rules

Each question should be:

- narrow;
- semantically coherent;
- answerable from supplied state;
- self-contained;
- explicit about output space/criteria;
- independent of hidden meaning in its key name.

If a question asks about a speculative branch, state the premise explicitly in the
question. Independent speculative questions can be batched; application code consumes
only the applicable answer.

Use a second request when a prior answer is necessary to fetch new evidence, construct a
new candidate set, or materially change the state.

## Candidate coverage

A bounded selector cannot choose a value that is absent. If the right answer may be
missing, include a no-match option or perform a presence/coverage judgment separately.
