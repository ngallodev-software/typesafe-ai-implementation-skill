# Failures, fallback, and security

**Classification:** PUBLIC-DERIVED / INTERNAL-RECOMMENDATION

## Failure classes

### Invalid local input

Reject before any API call. Examples: malformed candidates, empty required state,
invalid policy config.

### Transport/service failure

Use supported SDK retry behavior for transient failures. After retry policy is exhausted,
apply the application's explicit fallback.

### Semantic uncertainty

A valid API response with diffuse/borderline probabilities. Do not classify as transport
failure and do not repeat the identical request merely to obtain a different judgment.

### No valid candidate

Handle explicitly with `none`/`other`/`no_match` where appropriate. Do not coerce the
highest-probability wrong candidate into authority.

### Policy rejection

A valid model answer can still be rejected by allowlists, authorization, lifecycle,
risk, or other deterministic policy.

## Credential boundary

- Skill scripts must run without a key.
- Do not ship `.env` or secret files in this skill.
- Keep runtime key server-side/external to the skill.
- Never place credentials in model state, receipts, logs, fixtures, or browser bundles.
- Do not log authorization headers.

## Data minimization

Send only evidence needed for the judgment. Apply the target organization's data-handling
rules before sending repository/customer/regulated data to a hosted service.

## Type safety limits

Typed output constrains the answer interface. It does not establish truth, permission,
source provenance, or policy compliance. Revalidate those in application code.
