#!/usr/bin/env python3
from __future__ import annotations

import argparse
from pathlib import Path

FILES = {
    "semantic_types.py": '''from __future__ import annotations
from dataclasses import dataclass
from typing import Any, Mapping

@dataclass(frozen=True)
class SemanticDecisionRequest:
    decision_set: str
    question_schema_version: str
    policy_version: str
    state: Mapping[str, Any]
    questions: Mapping[str, Any]
    model: str | None = None

@dataclass(frozen=True)
class SemanticDecisionResult:
    model: str | None
    answers: Mapping[str, Any]
    transport_failed: bool = False
    error_kind: str | None = None
''',
    "typesafe_adapter.py": '''from __future__ import annotations
from .semantic_types import SemanticDecisionRequest, SemanticDecisionResult

class TypeSafeDecisionClient:
    """Thin optional adapter. Contains no business policy and no credentials."""

    def evaluate(self, request: SemanticDecisionRequest) -> SemanticDecisionResult:
        from typesafe_sdk import TypeSafeClient

        kwargs = {"state": dict(request.state), "questions": dict(request.questions)}
        if request.model is not None:
            kwargs["model"] = request.model

        with TypeSafeClient() as client:
            response = client.system_one(**kwargs)

        return SemanticDecisionResult(
            model=getattr(response, "model", request.model),
            answers=getattr(response, "answers", {}),
        )
''',
    "semantic_policy.py": '''from __future__ import annotations

def decide(result, policy):
    """Application-owned policy. Replace placeholders with calibrated rules."""
    if result.transport_failed:
        return policy.transport_fallback
    return policy.advisory_outcome
''',
    "README.semantic.md": '''# Semantic decision integration scaffold

This scaffold intentionally contains no TypeSafe credential. Configure live credentials
through the host application's existing runtime secret/config mechanism.

Before enabling automation:
1. implement a bounded state projector;
2. version question sets;
3. normalize current SDK response types;
4. implement explicit fallback/policy;
5. add fake/offline tests;
6. shadow and calibrate on representative cases.
''',
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
        path.write_text(content, encoding="utf-8")
        print(path)


if __name__ == "__main__":
    main()
