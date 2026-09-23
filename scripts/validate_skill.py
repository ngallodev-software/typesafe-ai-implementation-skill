#!/usr/bin/env python3
from __future__ import annotations

import json
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]

REQUIRED = [
    ROOT / "SKILL.md",
    ROOT / "INTERNAL.md",
    ROOT / "references" / "00-provenance.md",
    ROOT / "references" / "12-public-source-index.md",
    ROOT / "assets" / "semantic-decision-receipt.schema.json",
]

errors: list[str] = []
for path in REQUIRED:
    if not path.exists():
        errors.append(f"missing required file: {path.relative_to(ROOT)}")

skill = (ROOT / "SKILL.md").read_text(encoding="utf-8") if (ROOT / "SKILL.md").exists() else ""
if not skill.startswith("---\n"):
    errors.append("SKILL.md missing YAML frontmatter")
if "name: typesafe-impl-internal" not in skill:
    errors.append("SKILL.md has wrong/missing internal skill name")
if "visibility: internal" not in skill:
    errors.append("SKILL.md missing visibility: internal")
if "credentials_required_by_skill: false" not in skill:
    errors.append("SKILL.md must declare credentials_required_by_skill: false")

for path in ROOT.rglob("*.json"):
    try:
        json.loads(path.read_text(encoding="utf-8"))
    except Exception as exc:
        errors.append(f"invalid JSON {path.relative_to(ROOT)}: {exc}")

for forbidden in (".env", ".env.local", "credentials.json", "secrets.json"):
    if any(p.name == forbidden for p in ROOT.rglob("*")):
        errors.append(f"forbidden secret/config file present: {forbidden}")

# Look for obvious key-value patterns, not the documented environment-variable name.
secret_patterns = [
    re.compile(r"(?i)(api[_-]?key|authorization)\s*[:=]\s*['\"]?[A-Za-z0-9_-]{20,}"),
    re.compile(r"(?i)bearer\s+[A-Za-z0-9._-]{20,}"),
]
for path in ROOT.rglob("*"):
    if not path.is_file() or path.suffix in {".zip", ".gz", ".tgz"}:
        continue
    try:
        text = path.read_text(encoding="utf-8")
    except UnicodeDecodeError:
        continue
    for pat in secret_patterns:
        if pat.search(text):
            errors.append(f"possible embedded credential in {path.relative_to(ROOT)}")
            break

if errors:
    print("typesafe-impl-internal validation FAILED")
    for error in errors:
        print(f"- {error}")
    sys.exit(1)

print("typesafe-impl-internal validation OK")
print("- YAML/internal markers present")
print("- JSON files parse")
print("- no forbidden secret files")
print("- no obvious embedded credential values")
