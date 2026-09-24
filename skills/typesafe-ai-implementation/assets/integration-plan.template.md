# TypeSafe integration plan

## Target seam

- Repository/component:
- Existing behavior:
- Why this is semantic rather than deterministic/generative:
- Existing authority that must remain unchanged:

## Evidence/state

- Inputs:
- Stable IDs/provenance:
- Sensitive fields to exclude/redact:
- Freshness requirements:

## Questions

| Key | Primitive | Meaning | Criteria / scale | Why separate? |
|---|---|---|---|---|
| | | | | |

## Harness placement

- StateProjector:
- QuestionSetRegistry:
- TypeSafeDecisionClient:
- DecisionReceipt:
- DecisionPolicy:
- Optional receipt store:
- Optional semantic eval harness:

## Runtime configuration

- Optional dependency strategy:
- Existing secret/config mechanism to use at runtime:
- Behavior when TypeSafe is disabled/unavailable:

## Policy and fallback

- Shadow/advisory/automation mode:
- No-match behavior:
- Semantic-uncertainty behavior:
- Transport-failure behavior:
- Post-selection deterministic checks:

## Tests/evals

- Offline unit tests:
- Live contract tests (optional):
- Semantic eval corpus:
- Metrics:
- Promotion criteria:
