# Evolution guide

Keep this file as a short, dated record of meaningful changes to the skill and plugin.
Append new entries rather than rewriting older decisions. For each update, record the
reason, the user-visible behavior or contract that changed, the authoritative docs checked,
and the validation performed. Keep full implementation detail in the skill and references.

## 2026-09-24 — ChatGPT and Codex plugin package

- Added the Jev AI Implementation plugin under `plugins/typesafe-ai-implementation/`,
  with a portable root `plugin.json`, a `.codex-plugin/plugin.json` compatibility
  manifest, and a repo marketplace at `.agents/plugins/marketplace.json`.
- Added the supplied Jev icon as the plugin composer icon.
- Clarified that the bundled skill helps ChatGPT/Codex build applications that call Jev;
  it does not replace the coding model or make API calls itself. The official TypeSafe
  agent skill and current vendor documentation remain authoritative for API behavior.
- Refined confidence guidance: use a Choice result directly when selecting the best
  option; add confidence gates when uncertainty or action risk changes application
  behavior; threshold Noul only when the application needs a binary policy.
- Linked the plugin and current TypeSafe references from the README and skill. Kept
  product/API behavior as a snapshot to be checked against live docs.
- Distribution is through the repository marketplace for local/repo use. Listing in the
  universal public Plugins Directory remains a separate submission/review step.
- The canonical skill now lives at `skills/typesafe-ai-implementation/`; the plugin
  bundles a synchronized copy of that package, including its provenance and notices.
  Keep the bundled `skills/typesafe-ai-implementation/` tree synchronized when updating
  the canonical skill, and check links from both locations.
- README installation guidance describes the desktop app workflow supported by this
  repository marketplace, instead of a Codex CLI subcommand unavailable in the tested
  CLI version.

### Sources checked

- [TypeSafe: Jev with coding agents](https://docs.typesafe.ai/introduction/coding-agents)
- [TypeSafe: Confidence](https://docs.typesafe.ai/confidence)
- [TypeSafe: Advanced structured questions](https://docs.typesafe.ai/primitives/advanced)
- [OpenAI: Package your plugin](https://developers.openai.com/plugins/build/plugins)
- [OpenAI: Plugins in ChatGPT and Codex](https://learn.chatgpt.com/docs/plugins?surface=app)

### Validation

- `validate_skill.py`, `quick_validate.py`, and `validate_plugin.py` passed on the
  canonical skill and repository plugin package.
- Portable plugin manifests and `.agents/plugins/marketplace.json` parsed as JSON; the
  marketplace source is the repo-relative `./plugins/typesafe-ai-implementation` path.
- `git diff --check` passed. The local personal plugin copy was synchronized and its
  cachebuster refreshed; its reinstall command is not available in the installed
  `codex-cli 0.31.0`, so the app may require a restart/new task to reload it.

## 2026-09-24 — Public Plugins Directory preparation

- Removed first-party Agent-Workflow, SpecGen, portfolio, and benchmark case studies
  from the skill and README so the plugin presents a general TypeSafe integration
  workflow. Retained maintainer identity and third-party notices.
- Added an OpenAI public-submission checklist. The plugin is skills-only, which OpenAI
  supports without an MCP server.
- Before public submission, the maintainer still needs a verified publisher identity,
  Apps Management write access, public listing/support/privacy/terms details, starter
  prompts, five positive and three negative test cases, availability regions, and
  release notes. Submission review and approval precede publication.

### Sources checked

- [OpenAI: Submit plugins](https://developers.openai.com/plugins/deploy/submission)
- [OpenAI: Plugin guidelines](https://developers.openai.com/plugins/app-guidelines)
- [OpenAI: Submission errors](https://developers.openai.com/plugins/deploy/submission-errors)

## 2026-09-24 — Public submission metadata and package polish

- Shortened the plugin subtitle to meet the 30-character directory limit and generated
  a companion square listing logo for the existing composer icon.
- Clarified in public listing copy that this is an independent guide, not an official
  TypeSafe product, and described its codebase-assessment and offline-scaffolding value.
- Corrected public snapshot wording and section numbering; removed experimental labels
  from the public listing and skill metadata.
- Added three starter prompts and five positive / three negative review cases. Clarified
  that URLs are optional for skills-only ZIP validation while privacy guidance expects
  a published policy.
- Bumped the plugin to 0.1.2 and the bundled skill to 0.1.1.
- Built `marketplace-submission/jev-ai-implementation-0.1.2.zip` with only plugin-root
  files and verified its manifests, skills directory, excluded repo marketplace, and
  archive integrity.
