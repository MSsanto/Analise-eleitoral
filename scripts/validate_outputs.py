from __future__ import annotations

import hashlib
import json
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]

required = [
    ROOT / "data/derived/snapshot-latest.json",
    ROOT / "data/derived/release-manifest.json",
    ROOT / "data/derived/candidaturas_por_cargo.csv",
    ROOT / "data/derived/deputado_estadual_por_uf.csv",
    ROOT / "data/derived/receitas_por_fonte.csv",
    ROOT / "data/derived/despesas_por_categoria.csv",
    ROOT / "docs/reports/latest.md",
]

missing = [str(path.relative_to(ROOT)) for path in required if not path.exists()]
if missing:
    raise SystemExit(f"Artefatos ausentes: {missing}")

snapshot = json.loads((ROOT / "data/derived/snapshot-latest.json").read_text(encoding="utf-8"))
assert snapshot["meta"]["analysis_schema_version"] >= 1
assert snapshot["meta"].get("source_repository") == "MSsanto/Elei-oes-2026"
assert "source_commit" in snapshot["meta"] or snapshot["meta"].get("pipeline_version") == "0.1.0"
assert snapshot["candidaturas"]["candidaturas_total"] > 0
assert snapshot["financas"]["total_receitas"] >= 0
assert snapshot["financas"]["total_despesas_contratadas"] >= 0
assert 0 <= snapshot["financas"]["concentracao_top10_despesas_percentual"] <= 100.0001
assert abs(sum(r["percentual"] for r in snapshot["financas"]["receitas_por_fonte"]) - 100) < 0.2

manifest_path = ROOT / "data/derived/release-manifest.json"
manifest = json.loads(manifest_path.read_text(encoding="utf-8"))
assert manifest["manifest_schema_version"] >= 1
assert re.match(r"^\d{8}T\d{6}Z-schema\d+-v\d+\.\d+\.\d+$", manifest["data_release_id"])
assert manifest["software_version"] == (ROOT / "VERSION").read_text(encoding="utf-8").strip()
assert manifest["analysis_schema_version"] == snapshot["meta"]["analysis_schema_version"]

for artifact in manifest.get("artifacts", []):
    path = ROOT / artifact["path"]
    if not path.exists():
        raise SystemExit(f"Artefato referenciado no manifesto não existe: {artifact['path']}")
    digest = hashlib.sha256(path.read_bytes()).hexdigest()
    if digest != artifact["sha256"]:
        raise SystemExit(f"SHA-256 divergente: {artifact['path']}")

if not any(a["path"] == "data/derived/snapshot-latest.json" for a in manifest.get("artifacts", [])):
    raise SystemExit("Manifesto de release não referencia snapshot-latest.json")

print("OK: artefatos, manifesto de release e invariantes mínimos validados")
