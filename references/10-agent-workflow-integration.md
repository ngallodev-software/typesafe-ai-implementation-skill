# Agent-Workflow integration opportunities

**Classification:** PROJECT-SPECIFIC / INTERNAL-DERIVED / INTERNAL-RECOMMENDATION

These notes derive from the internal review of `ngallodev-software/agent-workflow` and
must be revalidated against the current repository before implementation.

## Preserve these authority boundaries

Do not replace deterministic evaluation/review/lifecycle authority such as:

- exact plan/contract validation;
- sealed evidence/receipt verification;
- scope/reference checks;
- hard review gates;
- lifecycle state and acknowledgement authority;
- allowlists/model policy.

In particular, an exact index/review gate should remain deterministic.

## Best first seam — routing enrichment

Current routing advice is deterministic and advisory while configured/enforced selection
remains authoritative. That is a strong semantic seam.

Potential TypeSafe questions from task text/context:

- Choice: semantic task type among validated task classes;
- Noul: interaction/user decision required?;
- Score: semantic/behavioral risk dimension.

Feed these as **advisory metadata** into the existing deterministic router. Never let
TypeSafe bypass allowed-model, no-go, executor, or enforced-selection policy.

## Skill semantic eval second pass

Keep existing deterministic regex/contract tests as the hard release gate. Add an
optional semantic assessment for whether a skill actually teaches the required behavior.
Run in shadow/advisory mode until calibrated.

## Evidence fidelity assistance

Where exact verification is impossible, use Noul judgments for semantic support or
contradiction between a claim and evidence. Keep checksum/schema/command/scope checks
deterministic.

## Review attention / inbox triage

Score/classify durable messages/events for attention, blocker likelihood, inconsistency,
or user-decision need. Do not change durable lifecycle/ack authority.

## Evaluation-plan diagnostics

Assess whether an evaluation meaningfully tests a requirement, whether an oracle is
semantically suitable, or where coverage appears weak. Keep structural validation and
sealed evaluation outcomes deterministic.

## Packaging

Prefer optional/lazy integration. A semantic plugin/extra or advisory artifact aligns
better than making TypeSafe a core dependency or lifecycle hook.
