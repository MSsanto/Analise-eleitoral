from __future__ import annotations

import json
from pathlib import Path

from analise_eleitoral.release import build_release_manifest, sha256_file

ROOT = Path(__file__).resolve().parents[1]


def test_versions_are_synchronized():
    version = (ROOT / "VERSION").read_text(encoding="utf-8").strip()
    assert f'version = "{version}"' in (ROOT / "pyproject.toml").read_text(encoding="utf-8")
    assert f'__version__ = "{version}"' in (ROOT / "src/analise_eleitoral/__init__.py").read_text(encoding="utf-8")
    assert f"[{version}]" in (ROOT / "CHANGELOG.md").read_text(encoding="utf-8")


def test_governance_required_docs_exist():
    cfg = json.loads((ROOT / "config/governance.json").read_text(encoding="utf-8"))
    for rel in cfg["required_documents"]:
        assert (ROOT / rel).exists(), rel


def test_release_manifest_hashes_snapshot():
    snapshot = json.loads((ROOT / "data/derived/snapshot-latest.json").read_text(encoding="utf-8"))
    manifest = build_release_manifest(snapshot, ROOT)
    row = next(a for a in manifest["artifacts"] if a["path"] == "data/derived/snapshot-latest.json")
    assert row["sha256"] == sha256_file(ROOT / row["path"])
    assert manifest["software_version"] == (ROOT / "VERSION").read_text(encoding="utf-8").strip()
