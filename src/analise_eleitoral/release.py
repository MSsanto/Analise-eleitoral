from __future__ import annotations

import hashlib
import json
from datetime import datetime, timezone
from pathlib import Path
from typing import Any


def sha256_file(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as fh:
        for chunk in iter(lambda: fh.read(1024 * 1024), b""):
            digest.update(chunk)
    return digest.hexdigest()


def _compact_utc(value: str) -> str:
    try:
        dt = datetime.fromisoformat(value.replace("Z", "+00:00"))
    except (TypeError, ValueError):
        dt = datetime.now(timezone.utc)
    if dt.tzinfo is None:
        dt = dt.replace(tzinfo=timezone.utc)
    return dt.astimezone(timezone.utc).strftime("%Y%m%dT%H%M%SZ")


def build_release_manifest(snapshot: dict[str, Any], output_root: Path) -> dict[str, Any]:
    derived = output_root / "data" / "derived"
    version = (output_root / "VERSION").read_text(encoding="utf-8").strip()
    generated = snapshot["meta"]["generated_at_utc"]
    schema = int(snapshot["meta"]["analysis_schema_version"])
    release_id = f"{_compact_utc(generated)}-schema{schema}-v{version}"

    # Núcleo do release: artefatos de dados/texto necessários para auditoria.
    # Gráficos e apresentações são produtos derivados regeneráveis e não bloqueiam
    # a publicação do snapshot se o núcleo de dados estiver íntegro.
    candidates = [
        derived / "snapshot-latest.json",
        derived / "candidaturas_por_cargo.csv",
        derived / "deputado_estadual_por_uf.csv",
        derived / "receitas_por_fonte.csv",
        derived / "despesas_por_categoria.csv",
        output_root / "docs" / "reports" / "latest.md",
    ]

    artifacts: list[dict[str, Any]] = []
    for path in candidates:
        if path.exists():
            artifacts.append({
                "path": str(path.relative_to(output_root)).replace("\\", "/"),
                "bytes": path.stat().st_size,
                "sha256": sha256_file(path),
            })

    manifest = {
        "manifest_schema_version": 1,
        "data_release_id": release_id,
        "generated_at_utc": generated,
        "software_version": version,
        "analysis_schema_version": schema,
        "source": {
            "repository": snapshot["meta"].get("source_repository"),
            "branch": snapshot["meta"].get("source_branch"),
            "commit": snapshot["meta"].get("source_commit"),
            "generated_at_utc": snapshot["meta"].get("source_generated_at_utc", {}),
        },
        "quality": {
            "manifest_checks_ok": all(v.get("ok") for v in snapshot.get("qualidade", {}).get("manifest_checks", {}).values()),
            "federal_uf_coverage_ok": snapshot.get("qualidade", {}).get("federal_ufs_presentes") == snapshot.get("qualidade", {}).get("federal_ufs_esperadas"),
            "alerts": [a for a in snapshot.get("qualidade", {}).get("alertas", []) if a],
        },
        "artifacts": artifacts,
    }
    return manifest


def write_release_manifest(snapshot: dict[str, Any], output_root: Path) -> Path:
    manifest = build_release_manifest(snapshot, output_root)
    path = output_root / "data" / "derived" / "release-manifest.json"
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(manifest, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    return path
