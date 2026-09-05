from __future__ import annotations

from datetime import datetime, timezone
from pathlib import Path
from typing import Any
import json


def _parse_dt(value: str | None) -> datetime | None:
    if not value:
        return None
    try:
        dt = datetime.fromisoformat(value.replace('Z', '+00:00'))
    except (TypeError, ValueError):
        return None
    if dt.tzinfo is None:
        dt = dt.replace(tzinfo=timezone.utc)
    return dt.astimezone(timezone.utc)


def freshness_report(snapshot: dict[str, Any], sla_hours: dict[str, int], now: datetime | None = None) -> dict[str, Any]:
    now = (now or datetime.now(timezone.utc)).astimezone(timezone.utc)
    generated = snapshot.get('meta', {}).get('source_generated_at_utc', {}) or {}
    sources: dict[str, Any] = {}
    overall_ok = True

    for name, max_hours in sla_hours.items():
        raw = generated.get(name)
        dt = _parse_dt(raw)
        if dt is None:
            sources[name] = {
                'generated_at_utc': raw,
                'age_hours': None,
                'sla_hours': max_hours,
                'ok': False,
                'reason': 'timestamp ausente ou inválido',
            }
            overall_ok = False
            continue
        age = max(0.0, (now - dt).total_seconds() / 3600.0)
        ok = age <= float(max_hours)
        sources[name] = {
            'generated_at_utc': raw,
            'age_hours': round(age, 3),
            'sla_hours': max_hours,
            'ok': ok,
            'reason': None if ok else 'fonte acima do SLA de atualização',
        }
        overall_ok = overall_ok and ok

    return {'ok': overall_ok, 'checked_at_utc': now.isoformat(), 'sources': sources}


def integrity_report(snapshot: dict[str, Any]) -> dict[str, Any]:
    manifest = snapshot.get('qualidade', {}).get('manifest_checks', {}) or {}
    failed = [office for office, row in manifest.items() if not bool(row.get('ok'))]
    federal_present = snapshot.get('qualidade', {}).get('federal_ufs_presentes')
    federal_expected = snapshot.get('qualidade', {}).get('federal_ufs_esperadas')
    federal_ok = bool(federal_expected) and federal_present == federal_expected
    total_ok = int(snapshot.get('candidaturas', {}).get('candidaturas_total') or 0) > 0
    return {
        'ok': not failed and federal_ok and total_ok,
        'manifest_failed': failed,
        'federal_uf_coverage_ok': federal_ok,
        'candidate_total_positive': total_ok,
    }


def publication_gate(snapshot: dict[str, Any], governance_config: dict[str, Any], now: datetime | None = None) -> dict[str, Any]:
    freshness = freshness_report(snapshot, governance_config.get('freshness_sla_hours', {}), now=now)
    integrity = integrity_report(snapshot)
    reasons: list[str] = []
    if not freshness['ok']:
        reasons.append('freshness gate reprovado')
    if not integrity['ok']:
        reasons.append('integrity gate reprovado')
    return {'ok': not reasons, 'reasons': reasons, 'freshness': freshness, 'integrity': integrity}


def quarantine_snapshot(snapshot: dict[str, Any], output_root: Path, gate: dict[str, Any]) -> Path:
    stamp = datetime.now(timezone.utc).strftime('%Y%m%dT%H%M%SZ')
    path = output_root / 'data' / 'quarantine' / f'{stamp}-snapshot-reprovado.json'
    path.parent.mkdir(parents=True, exist_ok=True)
    payload = {'gate': gate, 'snapshot': snapshot}
    path.write_text(json.dumps(payload, ensure_ascii=False, indent=2) + '\n', encoding='utf-8')
    return path
