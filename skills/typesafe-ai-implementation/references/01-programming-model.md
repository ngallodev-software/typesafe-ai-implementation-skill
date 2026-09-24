# Programming model

**Classification:** PUBLIC-DERIVED / PROJECT-GUIDANCE

TypeSafe System One should be treated as a typed semantic decision layer. The
application supplies state and bounded questions; the application continues to own
workflow, policy, side effects, persistence, authorization, and deterministic checks.

## Decision taxonomy

Use four buckets when inspecting a codebase:

### Deterministic

Exact outcome can be calculated from known inputs. Keep in code.

Examples: schema validation, permissions/allowlists, reference integrity, digests,
arithmetic, path safety, state-machine legality, cryptographic checks.

### Semantic bounded

A knowledgeable reviewer can make a narrow judgment from supplied evidence without
research or a long plan. Strong System One candidate.

Examples: intent classification, relevance, ambiguity, semantic support, qualitative
risk dimension, bounded handler selection.

### Generative/reasoning

Requires synthesis, new text/code, research, dependent planning, or explanation. Use a
reasoning/generative model. TypeSafe can still narrow, gate, rank, or verify pieces.

### Authority-bearing

Outcome grants permission, accepts work, mutates durable lifecycle state, or performs
irreversible/high-consequence action. Semantic judgments may inform policy but should
not silently become authority.

## Design invariant

> Model output is evidence. Application code decides how that evidence affects behavior.

This invariant lets the integration evolve without coupling vendor output directly to
business authority.
