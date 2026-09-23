# INTERNAL — do not publish as-is

`typesafe-impl-internal` is an internal working skill assembled from:

1. public TypeSafe documentation / SDK interfaces;
2. a TypeSafe skill snapshot supplied by the user;
3. implementation analysis derived for this work;
4. project-specific analysis of Agent-Workflow and SpecGen.

It intentionally contains material that has **not yet been reduced to a public-source-only
provenance set**. Nothing here contains an API key or other runtime credential, but this
package should not be pushed to a public repository as-is.

For future public extraction, every reference file uses one or more provenance tags:

- `PUBLIC-SOURCE` — factual contract intended to be traceable to public TypeSafe material.
- `PUBLIC-DERIVED` — engineering restatement/organization derived from public interfaces.
- `INTERNAL-DERIVED` — analysis synthesized during this project and not yet source-cleared.
- `INTERNAL-RECOMMENDATION` — our architecture/testing recommendation.
- `PROJECT-SPECIFIC` — analysis tied to the user's applications/repositories.

The future `typesafe-impl-public` should retain only material that is either original
implementation guidance or can be independently supported by public sources and licenses.
