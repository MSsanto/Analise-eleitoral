from __future__ import annotations

import json
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SEMVER = re.compile(r"^(0|[1-9]\d*)\.(0|[1-9]\d*)\.(0|[1-9]\d*)$")

cfg = json.loads((ROOT / "config/governance.json").read_text(encoding="utf-8"))
version = (ROOT / cfg["software_version_file"]).read_text(encoding="utf-8").strip()

if not SEMVER.match(version):
    raise SystemExit(f"VERSION inválida para SemVer: {version}")

pyproject = (ROOT / "pyproject.toml").read_text(encoding="utf-8")
init_py = (ROOT / "src/analise_eleitoral/__init__.py").read_text(encoding="utf-8")
changelog = (ROOT / cfg["changelog_file"]).read_text(encoding="utf-8")

checks = {
    "pyproject": f'version = "{version}"' in pyproject,
    "__version__": f'__version__ = "{version}"' in init_py,
    "changelog": f"[{version}]" in changelog,
}
for name, ok in checks.items():
    if not ok:
        raise SystemExit(f"Versão {version} não sincronizada em {name}")

missing = [p for p in cfg.get("required_documents", []) if not (ROOT / p).exists()]
if missing:
    raise SystemExit(f"Documentos de governança ausentes: {missing}")

backlog = (ROOT / cfg["backlog_file"]).read_text(encoding="utf-8")
if "AE-GOV-001" not in backlog or "P0" not in backlog:
    raise SystemExit("Backlog canônico não contém estrutura mínima de IDs/prioridade")

adr_dir = ROOT / "docs/ADRS"
if not adr_dir.exists() or not list(adr_dir.glob("[0-9][0-9][0-9][0-9]-*.md")):
    raise SystemExit("Nenhum ADR versionado encontrado")

print(f"OK: governança válida; software v{version}; {len(cfg['required_documents'])} documentos obrigatórios")
