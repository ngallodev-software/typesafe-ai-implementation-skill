#!/usr/bin/env python3
from __future__ import annotations

import argparse
from pathlib import Path

FILES = {
  "semantic-types.ts": """export interface SemanticDecisionRequest {\n  decisionSet: string;\n  questionSchemaVersion: string;\n  policyVersion: string;\n  state: unknown;\n  questions: Record<string, unknown>;\n  model?: string;\n}\n\nexport interface SemanticDecisionResult {\n  model?: string;\n  answers: Record<string, unknown>;\n  transportFailed: boolean;\n  errorKind?: string;\n}\n""",
  "typesafe-adapter.ts": """import type { SemanticDecisionRequest, SemanticDecisionResult } from './semantic-types';\n\n/** Thin adapter only. Bind to @typesafe-ai/sdk after checking the current SDK API. */\nexport class TypeSafeDecisionClient {\n  async evaluate(_request: SemanticDecisionRequest): Promise<SemanticDecisionResult> {\n    throw new Error('Bind this scaffold to the current @typesafe-ai/sdk in the host repository');\n  }\n}\n""",
  "semantic-policy.ts": """import type { SemanticDecisionResult } from './semantic-types';\n\nexport function decide(result: SemanticDecisionResult, policy: any): unknown {\n  if (result.transportFailed) return policy.transportFallback;\n  return policy.advisoryOutcome;\n}\n""",
  "README.semantic.md": """# Semantic decision integration scaffold\n\nNo API key belongs in this scaffold. Configure runtime credentials through the host\napplication's normal secret/config mechanism. Keep policy/authority outside the adapter.\n""",
}

def main() -> None:
    p = argparse.ArgumentParser()
    p.add_argument("target", type=Path)
    args = p.parse_args()
    args.target.mkdir(parents=True, exist_ok=True)
    for name, content in FILES.items():
        path = args.target / name
        if path.exists():
            raise SystemExit(f"refusing to overwrite {path}")
        path.write_text(content)
        print(path)

if __name__ == "__main__":
    main()
