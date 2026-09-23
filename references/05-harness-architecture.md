# Harness architecture

**Classification:** INTERNAL-DERIVED / INTERNAL-RECOMMENDATION

The default internal reference architecture is intentionally small.

```text
StateProjector
    |
    v
QuestionSetRegistry
    |
    v
TypeSafeDecisionClient
    |
    v
DecisionReceipt
    |
    v
DecisionPolicy
    |
    +--> existing behavior
    +--> deeper reasoning/human
    +--> advisory only
```

## StateProjector

Selects, normalizes, bounds, redacts, and provenance-tags source state. It should be
deterministically testable.

## QuestionSetRegistry

Owns versioned Choice/Noul/Score definitions. Do not bury question text inside random
call sites when the judgment is important enough to calibrate.

## TypeSafeDecisionClient

Thin vendor adapter:

- invokes the current official SDK/API;
- accepts projected state + question set + selected model/config;
- normalizes answer shapes;
- separates transport/service errors from valid semantic answers;
- exposes optional usage/latency;
- does not decide business thresholds.

## DecisionReceipt

Stable application-owned evidence envelope. It decouples downstream code from vendor
response objects and supports audit/evaluation.

## DecisionPolicy

Consumes raw semantic evidence and applies application rules:

- thresholds;
- composition across multiple judgments;
- fallback/escalation;
- post-selection allowlist/authority validation;
- whether a result is advisory or may automate a bounded action.

## Optional DecisionReceiptStore

Store only what is useful for reproducibility/evaluation. Prefer hashes and stable source
references when raw state is sensitive.

## Optional SemanticEvalHarness

Runs representative cases, current-vs-TypeSafe shadow comparisons, calibration,
consequence analysis, and regression checks.

## Dependency isolation

If TypeSafe is optional to the product, keep it optional:

- lazy import or optional package extra;
- no startup failure when absent;
- no automatic network call on normal deterministic paths;
- no change to authoritative behavior when disabled;
- explicit configuration/capability detection.
