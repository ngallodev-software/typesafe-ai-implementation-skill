---
name: typesafe-ai-implementation
description: >
  Codex companion playbook for integrating TypeSafe AI / Jev into software. Use to find
  bounded semantic decisions in a codebase and implement an appropriately small integration
  while keeping application policy and deterministic authority in code. Consult current
  TypeSafe docs and SDKs for vendor contracts.
license: Apache-2.0
metadata:
  visibility: public
  status: experimental
  version: 0.1.0
  source_scope: public-vendor-sources-and-project-derived-guidance
  credentials_required_by_skill: false
---

# TypeSafe AI Implementation Skill

This is a **Codex coding-agent skill for building applications that call Jev**. It does
not turn Codex into a Jev-powered coding model, replace Codex's language model, or call the
TypeSafe API itself. TypeSafe publishes an [official agent skill](https://docs.typesafe.ai/agent-skill)
for API, primitive, and pattern details; use that skill and the live docs as the vendor
reference. This companion focuses on codebase assessment, integration boundaries, and
project-owned policy. Any API examples or snapshots here are secondary and must be checked
against the current docs and SDK before implementation.

This is an **implementation and integration guide**, not a TypeSafe client. It works
without credentials and does not replace TypeSafe's official agent skill or live docs.
Never ask the user to paste an API key, expose its value, or copy it into generated files,
fixtures, receipts, logs, or source control. If the user explicitly requests live
experiments and the target environment already has runtime credentials, the official SDK
may consume them through the project's normal configuration. Keep calls scoped to the
request and minimize state sent to the API.

## Publication and provenance

This is a public, experimental implementation guide. It separates public TypeSafe
contracts from independently authored implementation patterns so readers can
distinguish vendor behavior from engineering judgment. See `PROVENANCE.md`,
`THIRD_PARTY_NOTICES.md`, and
`references/00-provenance.md`.

## Core operating rule

Use Jev where software needs a **bounded semantic judgment**. Keep exact rules,
validation, authorization, workflow state, persistence, side effects, arithmetic,
cryptographic checks, and other deterministic authority in ordinary code.

A useful mental model is:

```text
existing application evidence/state
        |
        v
project + redact + bound
        |
        v
TypeSafe typed judgments
Choice / Noul / Score
        |
        v
raw probabilities / distributions
        |
        v
application-owned policy
        |
        +--> existing deterministic path
        +--> advisory result
        +--> deeper reasoning / human escalation
```

Jev supplies typed semantic judgments, not free-form text or code generation. It can
replace fragile semantic extraction or an LLM prompt that asks for structured output when
typed questions with structured instructions or criteria fit. Keep exact parsing and validation
deterministic when they already solve the problem. Jev should add judgment at a real seam,
not become a generic model layer, workflow engine, or authorization engine.

## Before implementation

1. Read the repository's architecture, contracts, tests, CLI/API surfaces, and authority
   boundaries before designing a TypeSafe integration.
2. Read `references/01-programming-model.md` and `references/05-harness-architecture.md`.
3. Read the current live TypeSafe docs and the SDK page for the language being used.
   Start from `references/12-public-source-index.md`.
4. Do not begin by adding a dependency or framework. First identify the semantic decision
   seam and decide whether Jev improves on deterministic code or an existing model.
6. Scale the design to the task: a small, low-risk integration may need only a focused SDK
   call and a clear caller-side branch. Add adapters, durable receipts, policy layers, and
   evaluation harnesses when the host architecture, audit needs, risk, or rollout requires
   them; do not build the reference architecture by default.

## Step 1 — Inventory decision seams

Search for places where the application currently:

- uses keyword/regex/heuristic logic to interpret meaning;
- asks a generative model to return JSON or extract bounded structured facts that could be
  represented with a supported TypeSafe question or structure primitive;
- calls a larger reasoning/generative model only to classify, rank, verify, or route;
- asks the user questions that repository/application evidence could answer;
- over-fetches evidence because relevance is difficult to judge cheaply;
- collapses multiple semantic dimensions into a single brittle score;
- has a deterministic candidate set but weak semantic selection;
- needs a fast first-stage gate before expensive reasoning;
- has advisory metadata that could be improved without changing authority.

For each candidate seam, classify it as one of:

- `DETERMINISTIC`: exact code can decide correctly from known inputs. Do not use Jev.
- `SEMANTIC_BOUNDED`: narrow judgment from supplied state. Strong TypeSafe candidate.
- `GENERATIVE_REASONING`: requires synthesis, planning, prose, code, or dependent
  multi-step reasoning. Use a reasoning/generative model; TypeSafe may still gate or
  narrow the task.
- `AUTHORITY_BEARING`: permissions, acceptance, irreversible action, lifecycle or
  security authority. TypeSafe may provide evidence/advice only unless an explicitly
  calibrated application policy safely consumes it.

Prefer seams that are `SEMANTIC_BOUNDED` and already have a deterministic downstream
contract.

## Step 2 — Define the application behavior first

Write the intended application-level behavior before model questions:

- What decision is the application trying to make?
- What exact inputs/evidence are already available?
- What output space is allowed?
- What happens on uncertainty?
- What happens if TypeSafe is unavailable?
- Which existing code remains authoritative?
- What consequence follows from a wrong judgment?

Do not let the model design its own authority boundary.

Use `assets/integration-plan.template.md` when a formal plan is useful.

## Step 3 — Design projected state

Create a narrow state projector. State should include the evidence a competent reviewer
needs for the question and nothing irrelevant.

Prefer named JSON fields with stable identifiers and provenance:

```json
{
  "request": {"id": "R1", "text": "..."},
  "candidate": {"id": "C17", "description": "..."},
  "policy": {"allowed_ids": ["C17", "C23"]},
  "evidence": [{"id": "E4", "source": "...", "fact": "..."}]
}
```

Requirements:

- preserve identity and relationships;
- include enough evidence to answer the judgment;
- preserve observed facts separately from inferred facts;
- make relevant policy/constraints explicit;
- carry stable candidate/source IDs;
- redact secrets and irrelevant sensitive data;
- bound payload size in application code;
- canonicalize if requests will be hashed/cached;
- re-check freshness before acting on a result derived from mutable state.

Read `references/04-state-and-question-design.md`.

## Step 4 — Decompose into typed judgments

Choose the primitive by what the answer means:

- **Choice** — exactly one answer from a known finite set.
- **Noul** — probability that one binary semantic proposition is true.
- **Score** — degree along one ordered, described dimension.

Do not hide several independently useful dimensions in one question. Batch independent
questions over the same state. If a question depends on an earlier answer because that
answer changes evidence or candidates, make a second request.

Question instructions must be self-contained; do not rely on the machine question key
for semantics. Include `none` / `other` / `no_match` when a Choice candidate set may be
incomplete.

Read `references/03-primitives.md` and
`references/04-state-and-question-design.md`.

## Step 5 — Design the harness boundary

The preferred integration has separate responsibilities:

```text
StateProjector
    -> QuestionSetRegistry
        -> TypeSafeDecisionClient
            -> normalized DecisionReceipt
                -> DecisionPolicy
                    -> existing application behavior
```

Add supporting pieces when the application needs them:

- `DecisionReceiptStore` for audit/evidence;
- `SemanticEvalHarness` for shadow evaluation and threshold calibration;
- a reasoning/human escalation path for uncertain/high-consequence cases.

The TypeSafe client adapter should only:

- accept projected state and a versioned question set;
- invoke the official SDK/API;
- normalize the typed response;
- expose transport/service failure distinctly;
- return raw semantic evidence.

It should **not** own business thresholds, workflow transitions, permissions, acceptance,
or irreversible side effects.

Read `references/05-harness-architecture.md`.

## Step 6 — Keep runtime credentials external

This skill must never require a TypeSafe key. Generated harness code may rely on the
normal TypeSafe runtime environment/configuration supported by the current SDK. Never
write credential values or create secret-bearing files. Document the expected variable
and the repository's normal secrets setup; add a blank example config only if the repo
already uses that convention.

When live integration is requested:

1. use the target project's existing secrets mechanism;
2. prefer the official SDK's standard runtime configuration;
3. never serialize credentials into state or receipts;
4. never log authorization headers;
5. keep browser/client bundles free of server credentials.

Do not make live API calls unless the user asks for live experimentation or contract
testing. If no live credentials are configured, complete useful offline work with
fixtures and fakes; live contract tests are optional.

## Step 7 — Define uncertainty and fallback before automation

A successful API response can still be semantically uncertain. Treat these separately:

- invalid local input;
- transport/service failure;
- semantic uncertainty;
- no valid candidate / no-match;
- policy rejection after a valid model judgment.

Do not retry an identical semantic request merely to obtain a different opinion.
Use the SDK's supported transport retry behavior, then apply the application's explicit
fallback.

For authority-bearing paths, the default fallback is the existing authority path or a
fail-closed/escalation behavior—not implicit approval.

Read `references/07-confidence-calibration-rollout.md` and
`references/08-failure-security.md`.

## Step 8 — Produce a stable receipt

Normalize raw TypeSafe output into an application-owned receipt. Recommended fields:

- decision-set/version;
- request hash;
- model identifier;
- question-set version;
- policy version;
- typed answers and distributions;
- source/provenance references;
- policy outcome;
- whether fallback/escalation was used;
- optional usage/latency metadata.

Do not store raw sensitive state when a content hash plus durable source references is
sufficient. Use `assets/semantic-decision-receipt.schema.json` as a starting point.

## Step 9 — Evaluate before promoting behavior

Use an explicit progression:

```text
shadow -> advisory -> guarded automation -> evidence-based expansion
```

Measure application consequences, not just primitive agreement. Curate representative
labeled/adjudicated examples. Track at least:

- confusion/accuracy where appropriate;
- precision/recall across Noul policy cutoffs, when the application thresholds Noul results;
- calibration/reliability;
- escalation rate;
- false-accept and false-reject consequences;
- disagreement with the current system;
- latency and request cost;
- stability under harmless paraphrase/format changes;
- high-confidence wrong cases.

Use the returned Choice answer directly when the task is simply to select the best option;
do not add a confidence cutoff by default. Use Choice/Score confidence or probability
gates when the application must distinguish answer certainty or regulate an action by
its consequences. Noul returns P(yes), so threshold it only when the application needs a
binary action policy. Thresholds belong to the application, should vary with the cost of
errors, and must be evaluated on representative data. Never choose production cutoffs
merely because a probability “looks high.”

Read `references/09-testing-and-evaluation.md`.

## Step 10 — Version what changes meaning

Version or otherwise fingerprint changes to:

- state projection;
- question instructions;
- Choice/Score criteria;
- model identifier;
- policy thresholds/composition;
- fallback rules;
- source-selection/retrieval strategy when it changes the evidence presented.

This makes semantic behavior auditable and lets shadow evaluations compare like with
like.

## Strong implementation patterns

Read `references/06-pattern-catalog.md`. Prefer these patterns when they fit:

1. semantic router over an application-owned allowlist;
2. ambiguity / user-decision gate;
3. evidence relevance reranker;
4. claim/evidence support check;
5. multi-dimensional quality/completeness assessment;
6. hierarchical classification;
7. bounded function/tool selection;
8. System-One -> System-Two/human cascade;
9. semantic review/attention triage;
10. branch-specific speculative questions whose premises are explicit.

## Anti-patterns

Do not:

- use Jev to generate prose, plans, specifications, or code;
- replace deterministic schema, permission, arithmetic, filesystem, cryptographic, or
  exact reference checks;
- allow a semantic answer to mutate authoritative state without application policy;
- invent identifiers, paths, tools, URLs, or arbitrary values when a validated
  candidate set can be supplied;
- treat Choice/Score confidence as authorization or truth;
- treat Noul `0.5` as medium severity;
- use one omnibus question for unrelated dimensions;
- hide product/policy decisions inside model instructions;
- hard-code demo thresholds, vendor pricing, latency, or model behavior into architecture;
- make the optional integration a mandatory import/runtime dependency unless the target
  product explicitly requires it.

## Working with an existing repository

Before changing code, determine:

- existing dependency/optional-extra conventions;
- configuration/secrets conventions;
- result/receipt/error types;
- plugin/extension seams;
- authoritative lifecycle/validation/review code;
- deterministic tests that must remain authoritative;
- current semantic heuristics or model calls to compare against;
- where artifacts/schemas/versioned contracts live.

Prefer the smallest integration that preserves those boundaries. Do not create a new
framework simply because this skill contains a reference architecture.

## Offline helpers

The scripts in `scripts/` require only the Python standard library and do not call
TypeSafe:

- `validate_skill.py` validates this package and checks for common secret-file mistakes;
- `reassemble_contract.py` rebuilds the split machine implementation contract;
- `scaffold_python_harness.py` creates a minimal Python semantic-decision boundary;
- `scaffold_typescript_harness.py` creates a minimal TypeScript semantic-decision boundary.

Scaffolds are starting points. Adapt them to the target repository rather than forcing
the target repository to match the scaffold.

## Completion criteria

A TypeSafe integration is not complete merely because an SDK call works. Before calling
it complete, verify that:

- the semantic seam is appropriate;
- deterministic authority remains explicit;
- state is bounded and provenance-aware;
- typed questions are narrow and versioned;
- no-match/uncertainty behavior exists where needed;
- the adapter contains no hidden business authority;
- fallback behavior is explicit;
- credentials remain external;
- receipts/observability are sufficient for diagnosis;
- offline tests do not require an API key;
- semantic eval cases exist for the behavior being automated;
- rollout level matches measured evidence.

## Further reading

For vendor behavior, consult the [TypeSafe documentation](https://docs.typesafe.ai/llms.txt),
[coding-agent guide](https://docs.typesafe.ai/introduction/coding-agents),
[official TypeSafe agent skill](https://docs.typesafe.ai/agent-skill),
[System One](https://docs.typesafe.ai/concepts/system-one.md), the
[typed primitives](https://docs.typesafe.ai/primitives.md), and the
[Python SDK](https://docs.typesafe.ai/sdk/python.md). Jev/System One is described in
the [TypeSafe announcement](https://typesafe.ai/blog/introducing-system-one-models-and-jev).
For package contents and provenance, see `README.md` and `PROVENANCE.md`.
