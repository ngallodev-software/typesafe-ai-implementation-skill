# Testing and evaluation

**Classification:** INTERNAL-DERIVED / INTERNAL-RECOMMENDATION

## Deterministic unit tests — no API key

Test:

- state projection/redaction;
- candidate construction;
- canonical request hashing;
- question-set/version selection;
- response normalization using fakes/fixtures;
- policy composition and thresholds;
- fallbacks;
- no-match handling;
- post-selection authority checks;
- receipt serialization/schema validation where applicable.

Normal unit tests should not call the hosted service.

## Optional live contract tests

Run only when runtime credentials are intentionally supplied to the test environment:

- Noul request;
- Choice request;
- Score request;
- mixed batched request;
- model selection;
- auth failure behavior;
- timeout/retry path;
- response parsing/forward compatibility.

## Semantic evaluation set

Curate cases with reviewed expected application behavior. Store enough source evidence to
explain failures. Include:

- straightforward positives/negatives;
- ambiguous borderline cases;
- missing evidence;
- contradictory evidence;
- no-valid-candidate cases;
- nearly synonymous candidates;
- prompt-like/untrusted text inside state;
- stale policy/evidence;
- high-confidence wrong examples;
- low-confidence correct examples;
- harmless paraphrases and field-order/format variations.

Evaluate the **whole application composition**, not only whether a primitive selected the
expected label.
