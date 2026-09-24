# Provenance and publication status

This repository is a public, experimental implementation guide maintained by
**ngallodev-software**. It is independent of TypeSafe AI and is not an official
TypeSafe product, skill, or endorsement.

The material is intentionally separated into four source classes:

- `PUBLIC-SOURCE` — factual behavior traceable to current public TypeSafe
  documentation, SDKs, or source.
- `PUBLIC-DERIVED` — independently written restatements of public behavior.
- `PROJECT-DERIVED` / `PROJECT-GUIDANCE` — original engineering analysis,
  patterns, architecture guidance, and testing recommendations produced for this
  repository.
- `PROJECT-SPECIFIC` — analysis of public ngallodev-software projects such as
  Agent-Workflow and SpecGen-AW.

Vendor behavior should always be checked against the current TypeSafe
documentation and SDK version in use. Project guidance is not a claim about
TypeSafe product guarantees.

The original working material was assembled with reference to public TypeSafe
documentation, public SDK interfaces, and TypeSafe's public agent-skills
repository. The public TypeSafe skills repository is MIT-licensed; attribution
and its license notice are preserved in `THIRD_PARTY_NOTICES.md`.

No API keys or runtime credentials are required by this skill. Live TypeSafe
credentials belong only in the consuming application's normal secret-management
boundary.
