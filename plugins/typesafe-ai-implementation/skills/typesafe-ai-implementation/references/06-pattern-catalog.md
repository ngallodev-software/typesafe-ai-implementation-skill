# Implementation pattern catalog

**Classification:** PUBLIC-DERIVED / PROJECT-DERIVED / PROJECT-GUIDANCE

## Semantic router

Input: request + validated candidates + relevant policy summary.
Primitive: Choice.
Output: selected candidate ID + distribution.
Application: revalidate ID, then call the existing handler when selection alone is
sufficient. Add a confidence gate/fallback only when uncertainty or action risk requires it.

## Ambiguity / user-decision gate

Primitive: one or more Nouls.
Questions can distinguish semantic ambiguity from missing product/policy authorization.
The model detects where a decision is required; it does not invent the decision.

## Evidence reranker

Pipeline:

```text
broad deterministic/lexical/graph retrieval
 -> TypeSafe relevance Score/Noul per candidate
 -> deterministic top-K
 -> reasoning model/human reads narrowed evidence
```

TypeSafe reduces context. It does not replace source evidence.

## Claim/evidence verification

State: claim + exact candidate evidence + provenance + applicable policy.
Primitive: Noul for support; optionally a separate Noul for contradiction.
Use exact deterministic verification instead whenever exact verification is possible.

## Multi-dimensional quality assessment

Use one Score per independent dimension such as:

- specificity;
- testability;
- evidence support;
- scope clarity;
- compatibility coverage.

Compose in code with explicit policy.

## Hierarchical classification

Coarse Choice -> branch-specific Choice. Useful for large taxonomies or when each branch
has distinct candidate definitions.

## Bounded function/tool selection

Code discovers and validates callable candidates. Choice selects among them. Typed or
deterministic code constructs/validates arguments. Do not let the model fabricate an
unknown executable target.

## System-One / System-Two cascade

Use TypeSafe for narrow judgments. Escalate uncertain, high-consequence,
missing-evidence, or compositionally complex cases when the application's policy calls
for it; define that behavior from the task's consequences rather than a generic cutoff.
Preserve receipts for both layers separately.

## Review/attention triage

Score/classify messages, findings, or evidence for attention, blocker likelihood,
semantic inconsistency, or user-decision need. Keep durable lifecycle/ack authority in
existing code.
