# Choice, Noul, and Score

**Classification:** PUBLIC-DERIVED / PROJECT-GUIDANCE

## Choice

Use when exactly one member of a known finite candidate set should be selected. TypeSafe
returns the selected option and a probability distribution over the supplied options.

Good fits: route, task class, handler, queue, known tool/function, candidate source,
coarse taxonomy branch.

Rules:

- supply the entire allowed candidate set;
- use stable candidate IDs;
- include `other`/`none`/`no_match` when coverage is uncertain;
- never use Choice to invent arbitrary paths, IDs, URLs, commands, or tools;
- revalidate the selected candidate locally before action;
- treat confidence as distribution concentration, not permission or truth.
- if the task is only to choose the best candidate, use the returned selection; add a
  confidence gate only when uncertainty should change the application behavior.

For very large candidate sets, narrow them first (retrieval/filtering/scoring or
hierarchical classification) rather than assuming a flat Choice is appropriate.

## Noul

Use for one binary semantic proposition. Its result is the probability of "yes".

Good fits: evidence supports claim, requirement is ambiguous, human decision required,
candidate is relevant, text conflicts with protected behavior.

Rules:

- ask one proposition per Noul;
- near `0.5` means uncertain yes/no, not medium severity;
- use separate Nouls for independent multi-label conditions;
- the application may threshold P(yes) when a binary action policy requires it; the
  primitive itself does not choose that policy.

## Score

Use for degree along one ordered dimension. TypeSafe returns a score over the ordered
levels and a probability distribution across them; treat the score as the expected
position on that rubric, not a precise measurement.

Good fits: relevance, specificity, testability, severity, urgency, completeness,
compatibility impact.

Rules:

- levels must be ordered and behaviorally distinct;
- describe every level in domain terms;
- do not merge unrelated dimensions into one score;
- for ranking, use a comparable rubric for each candidate and sort in deterministic code;
- interpret the result as a probabilistic expectation, not exact measurement.
