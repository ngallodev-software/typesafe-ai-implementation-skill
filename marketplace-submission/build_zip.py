#!/usr/bin/env python3
"""Build the skills-only ZIP for OpenAI directory submission."""

from __future__ import annotations

import json
from pathlib import Path
from zipfile import ZIP_DEFLATED, ZipFile

ROOT = Path(__file__).resolve().parents[1]
PLUGIN = ROOT / "plugins" / "typesafe-ai-implementation"
DEST = ROOT / "marketplace-submission" / "typesafe-ai-implementation-0.1.4.zip"

manifest = json.loads((PLUGIN / ".codex-plugin" / "plugin.json").read_text(encoding="utf-8"))
if manifest["version"] != "0.1.4":
    raise SystemExit("Update DEST and release notes for the current plugin version before packaging")

with ZipFile(DEST, "w", compression=ZIP_DEFLATED, compresslevel=9) as archive:
    for path in sorted(PLUGIN.rglob("*")):
        if not path.is_file():
            continue
        if path.is_symlink():
            raise SystemExit(f"Refusing symlink in plugin package: {path}")
        archive.write(path, path.relative_to(PLUGIN).as_posix())

print(DEST)
