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
