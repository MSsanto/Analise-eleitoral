from __future__ import annotations

import json
from pathlib import Path
from typing import Any, Iterable


def load_json(path: Path) -> Any:
    with path.open("r", encoding="utf-8") as fh:
        return json.load(fh)


def write_json(path: Path, payload: Any) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("w", encoding="utf-8") as fh:
        json.dump(payload, fh, ensure_ascii=False, indent=2, sort_keys=False)
        fh.write("\n")


def _stamp_cargo(records: Iterable[dict[str, Any]], canonical: str) -> list[dict[str, Any]]:
    out: list[dict[str, Any]] = []
    for raw in records:
        item = dict(raw)
        item["cargo_analise"] = canonical
        out.append(item)
    return out


def load_candidates(source_root: Path) -> tuple[list[dict[str, Any]], dict[str, int]]:
    processed = source_root / "data" / "processed"
    base = processed / "candidatos"
    records: list[dict[str, Any]] = []
    expected: dict[str, int] = {}

    p_manifest = load_json(base / "presidente" / "manifest.json")
    p_file = base / "presidente" / p_manifest.get("arquivo", "brasil.json")
    p_records = _stamp_cargo(load_json(p_file), "Presidente")
    records.extend(p_records)
    expected["Presidente"] = int(p_manifest.get("total", len(p_records)))

    for slug, canonical in (("governador", "Governador"), ("senador", "Senador")):
        manifest = load_json(base / slug / "manifest.json")
        office_records: list[dict[str, Any]] = []
        for uf, cfg in manifest.get("ufs", {}).items():
            filename = cfg.get("arquivo", f"{uf}.json")
            path = base / slug / filename
            if not path.exists():
                path = base / slug / uf / filename
            office_records.extend(_stamp_cargo(load_json(path), canonical))
        records.extend(office_records)
        expected[canonical] = int(manifest.get("total", len(office_records)))

    federal_path = processed / "deputados_federais.json"
    federal = _stamp_cargo(load_json(federal_path), "Deputado Federal")
    records.extend(federal)
    metadata = load_json(processed / "metadata.json")
    expected["Deputado Federal"] = int(metadata.get("records", len(federal)))

    s_manifest = load_json(base / "deputado-estadual" / "manifest.json")
    state_records: list[dict[str, Any]] = []
    for uf, cfg in s_manifest.get("ufs", {}).items():
        uf_manifest_path = base / "deputado-estadual" / cfg["manifest"]
        uf_manifest = load_json(uf_manifest_path)
        pattern = uf_manifest.get("profiles_pattern", "perfis/{page:03d}.json")
        for page in range(1, int(uf_manifest.get("page_count", 0)) + 1):
            rel = pattern.format(page=page)
            page_records = load_json(uf_manifest_path.parent / rel)
            state_records.extend(_stamp_cargo(page_records, "Deputado Estadual/Distrital"))
    records.extend(state_records)
    expected["Deputado Estadual/Distrital"] = int(s_manifest.get("total", len(state_records)))
    return records, expected


def iter_finance_records(source_root: Path) -> Iterable[dict[str, Any]]:
    shard_dir = source_root / "data" / "processed" / "financas-2026" / "shards"
    if not shard_dir.exists():
        return
    for path in sorted(shard_dir.glob("*.json")):
        payload = load_json(path)
        if isinstance(payload, dict):
            yield from payload.values()


def load_source_metadata(source_root: Path) -> dict[str, Any]:
    processed = source_root / "data" / "processed"
    base = processed / "candidatos"
    payload: dict[str, Any] = {
        "candidate_manifest": load_json(base / "manifest.json"),
        "federal_metadata": load_json(processed / "metadata.json"),
    }
    optional = {
        "finance_manifest": processed / "financas-2026" / "manifest.json",
        "finance_overview": processed / "editorial" / "finance-overview.json",
        "camara_metadata": processed / "camara" / "metadata.json",
        "radar": processed / "editorial" / "radar.json",
    }
    for key, path in optional.items():
        if path.exists():
            payload[key] = load_json(path)
    return payload
