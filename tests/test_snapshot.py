import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]


def test_baseline_snapshot_consistency():
    snapshot = json.loads((ROOT / "data/derived/snapshot-latest.json").read_text(encoding="utf-8"))
    total = snapshot["candidaturas"]["candidaturas_total"]
    by_office = sum(row["total"] for row in snapshot["candidaturas"]["candidaturas_por_cargo"])
    assert total == by_office


def test_no_candidate_ranking_in_policy():
    config = json.loads((ROOT / "config/analysis.json").read_text(encoding="utf-8"))
    assert config["policy"]["candidate_rankings"] is False
    assert config["policy"]["political_scoring"] is False
