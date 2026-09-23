# Provenance model

**Classification:** INTERNAL-DERIVED / INTERNAL-RECOMMENDATION

This skill separates factual vendor contracts from our engineering guidance so later
public extraction is mechanical rather than editorial guesswork.

## Tags

| Tag | Meaning | Public candidate? |
|---|---|---|
| `PUBLIC-SOURCE` | Directly traceable to public TypeSafe docs/SDK/source | Yes, subject to license/quotation limits |
| `PUBLIC-DERIVED` | Our restatement of public behavior | Usually |
| `INTERNAL-DERIVED` | Analysis produced in this work | Review first |
| `INTERNAL-RECOMMENDATION` | Our integration architecture or operational advice | Yes if independently authored and appropriate |
| `PROJECT-SPECIFIC` | Agent-Workflow / SpecGen observations or recommendations | Only if repository/source context is public and intentionally disclosed |

## Source hierarchy

For implementation-time facts, prefer in this order:

1. live TypeSafe docs;
2. currently installed/selected official SDK reference and types;
3. official public SDK repository;
4. public TypeSafe examples/cookbooks;
5. this internal snapshot.

Version-dependent details in this skill are snapshots, not permanent guarantees.
