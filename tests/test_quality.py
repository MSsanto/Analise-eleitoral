from datetime import datetime, timezone, timedelta
from pathlib import Path
import json

from analise_eleitoral.quality import freshness_report, publication_gate, quarantine_snapshot


def _snapshot(ts: str):
    return {
        'meta': {'source_generated_at_utc': {'candidaturas': ts, 'financas': ts, 'camara': ts}},
        'candidaturas': {'candidaturas_total': 10},
        'qualidade': {
            'manifest_checks': {'Presidente': {'ok': True}},
            'federal_ufs_presentes': 27,
            'federal_ufs_esperadas': 27,
        },
    }


def test_freshness_passes_inside_sla():
    now = datetime(2026, 9, 5, 12, tzinfo=timezone.utc)
    ts = (now - timedelta(hours=1)).isoformat()
    report = freshness_report(_snapshot(ts), {'candidaturas': 12, 'financas': 18, 'camara': 36}, now)
    assert report['ok'] is True


def test_freshness_fails_when_stale():
    now = datetime(2026, 9, 5, 12, tzinfo=timezone.utc)
    ts = (now - timedelta(hours=40)).isoformat()
    report = freshness_report(_snapshot(ts), {'candidaturas': 12, 'financas': 18, 'camara': 36}, now)
    assert report['ok'] is False
    assert report['sources']['candidaturas']['ok'] is False


def test_publication_gate_and_quarantine_preserve_latest(tmp_path: Path):
    now = datetime(2026, 9, 5, 12, tzinfo=timezone.utc)
    stale = (now - timedelta(hours=50)).isoformat()
    snapshot = _snapshot(stale)
    gate = publication_gate(snapshot, {'freshness_sla_hours': {'candidaturas': 12, 'financas': 18, 'camara': 36}}, now)
    latest = tmp_path / 'data/derived/snapshot-latest.json'
    latest.parent.mkdir(parents=True)
    latest.write_text('{"sentinel": true}\n', encoding='utf-8')
    quarantine = quarantine_snapshot(snapshot, tmp_path, gate)
    assert quarantine.exists()
    assert json.loads(latest.read_text(encoding='utf-8')) == {'sentinel': True}
