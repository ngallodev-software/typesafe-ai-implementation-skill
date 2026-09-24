# Confidence, calibration, and rollout

**Classification:** PUBLIC-DERIVED / PROJECT-GUIDANCE

## Confidence is not authority

Choice/Score confidence describes concentration of the answer distribution. It does not
prove correctness, authorization, or application safety. A Noul already expresses the
probability of yes; treat values near 0.5 as semantic uncertainty.

When a Choice task only needs the best available option, use the returned choice without
adding a confidence cutoff by default. Add a confidence gate when uncertainty should
change what the application does. For Score, use the score/distribution for the intended
comparison, and gate an action only when its risk policy calls for one. For Noul, choose a
P(yes) cutoff only when the host application needs a binary action policy. TypeSafe's
[confidence guide](https://docs.typesafe.ai/confidence) describes confidence as a
convenient summary of the Choice/Score distribution; retain the full probabilities when
the application needs a different measure.

## Policy owns thresholds

Keep thresholds out of the vendor adapter. A policy object/function should decide:

- automation vs advisory;
- escalation threshold;
- no-match behavior;
- minimum evidence support;
- high-risk override;
- transport fallback.

## Calibrate on representative cases

Do not add a threshold where the application has no uncertainty-dependent behavior. When
a gate is warranted, do not select a production cutoff because `0.8` sounds confident.
Measure outcomes on representative labeled/adjudicated data and choose thresholds based
on application consequences.

Useful measurements:

- confusion matrices where applicable;
- precision/recall across thresholds;
- calibration/reliability curves;
- false-accept vs false-reject cost;
- coverage/escalation rate;
- disagreement with current behavior;
- stability under paraphrase/state formatting;
- latency/cost.

## Rollout ladder

1. **Shadow** — run TypeSafe beside current behavior; no user-visible effect.
2. **Advisory** — surface semantic evidence to existing decision makers/agents.
3. **Guarded automation** — automate bounded low-consequence paths under explicit policy.
4. **Evidence-based expansion** — expand only where measured results justify it.

Version the state projector, question set, model ID, and policy so evaluation results are
comparable.
