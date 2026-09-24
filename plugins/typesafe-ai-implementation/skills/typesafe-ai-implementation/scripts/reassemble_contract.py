#!/usr/bin/env python3
from __future__ import annotations

import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
C = ROOT / "references" / "contracts"

meta = json.loads((C / "00-meta-and-sources.json").read_text())
combined = {
    "schema": meta["schema"],
    "generated_at": meta["generated_at"],
    "purpose": meta["purpose"],
    "design_invariant": meta["design_invariant"],
    "sources": meta["sources"],
    "api": json.loads((C / "01-api.json").read_text()),
    "primitives": json.loads((C / "02-primitives.json").read_text()),
}
combined.update(json.loads((C / "03-question-and-state-design.json").read_text()))
combined["reference_feature"] = json.loads((C / "04-reference-harness.json").read_text())
combined.update(json.loads((C / "05-feature-patterns.json").read_text()))
combined.update(json.loads((C / "06-failure-and-security.json").read_text()))
combined.update(json.loads((C / "07-calibration-and-tests.json").read_text()))
combined.update(json.loads((C / "08-anti-patterns-and-checklist.json").read_text()))
combined["vendor_claims_snapshot_2026_09_14"] = json.loads((C / "09-vendor-claims-snapshot.json").read_text())

out = ROOT / "typesafe-implementation-contract.reassembled.json"
out.write_text(json.dumps(combined, indent=2) + "\n")
print(out)
