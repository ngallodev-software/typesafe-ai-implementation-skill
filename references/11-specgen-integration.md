# SpecGen integration opportunities

**Classification:** PROJECT-SPECIFIC / PROJECT-DERIVED / PROJECT-GUIDANCE

These notes derive from the project review of `ngallodev-software/specgen-aw` and must
be revalidated against the current repository before implementation.

SpecGen's canonical JSON, append-only decisions, deterministic validation, repository
evidence, and finalization rules should remain authoritative.

## Preferred boundary — separate semantic assessment artifact

Add a separate artifact such as `specgen/semantic-assessment/v1alpha1` rather than
mixing probabilistic judgments into canonical deterministic repository evidence.

Suggested fields:

- canonical snapshot digest;
- question-set/state-projection versions;
- TypeSafe request digest/model ID;
- per-requirement typed judgments/distributions;
- evidence refs;
- advisory diagnostics;
- optional policy outcome.

## Semantic elicitation

For each requirement, possible batched judgments:

- Noul: materially ambiguous?;
- Noul: requires an unstated user/product/policy decision?;
- Noul: observable behavior sufficiently specified?;
- Noul: tension with a protected/preservation claim?;
- Score: testability from acceptance/evaluation intent?;
- Score: support from cited repository evidence?

TypeSafe identifies where clarification is needed. It should not invent the missing
product decision.

## Brownfield focus ranking

After deterministic discovery/graph narrowing, score candidate focus areas for relevance
and investigate top-K. Relevance/connectivity does not authorize scope expansion.

## User-question vs repository-research routing

Use Choice over a validated taxonomy such as:

- `user_decision`;
- `repository_answerable`;
- `external_research`;
- `already_supported`;
- `unclear`.

This can reduce unnecessary user questions while preventing silent product decisions.

## Repository evidence relevance

After deterministic evidence discovery, apply relevance Score/Noul judgments against
requirements/preservation/questions. Keep deterministic repository-analysis artifacts
separate from semantic assessment.

## Requirement quality dimensions

Score independent dimensions such as specificity, testability, evidence support, scope
clarity, and compatibility coverage. Use Noul for ambiguity/hidden decision flags.

## Semantic duplicate/conflict detection

Prefilter requirement pairs structurally/lexically, then use semantic equivalence,
overlap, or contradiction judgments. Treat findings as diagnostics until resolved by
canonical/user-authorized decisions.

## Evaluation-intent assistance

Choose among a code-discovered supported scorer/evaluation family; do not let TypeSafe
invent an unsupported scorer or change execution semantics.
