# Provenance model

**Classification:** PROJECT-DERIVED / PROJECT-GUIDANCE

This skill separates factual vendor contracts from independently authored engineering
guidance so source boundaries remain explicit and reviewable.

## Tags

| Tag | Meaning | Public candidate? |
|---|---|---|
| `PUBLIC-SOURCE` | Directly traceable to public TypeSafe docs/SDK/source | Yes, subject to license/quotation limits |
| `PUBLIC-DERIVED` | Our restatement of public behavior | Usually |
| `PROJECT-DERIVED` | Original analysis produced for this repository | Yes; distinguish it from vendor claims |
| `PROJECT-GUIDANCE` | Original integration architecture or operational advice | Yes; engineering judgment, not vendor contract |

## Source hierarchy

For implementation-time facts, prefer in this order:

1. live TypeSafe docs;
2. currently installed/selected official SDK reference and types;
3. official public SDK repository;
4. public TypeSafe examples/cookbooks;
5. this guide's documented snapshot.

Version-dependent details in this skill are snapshots, not permanent guarantees.
