from __future__ import annotations

import argparse
import json
from datetime import date
from pathlib import Path

from .charts import build_all_charts
from .pipeline import build_snapshot, write_snapshot_bundle
from .quality import publication_gate, quarantine_snapshot
from .presentation import build_presentation
from .report import write_report
from .release import write_release_manifest


def main() -> int:
    parser = argparse.ArgumentParser(description="Gera a camada analítica do projeto Eleições 2026")
    group = parser.add_mutually_exclusive_group(required=True)
    group.add_argument("--source", type=Path, help="Checkout local de MSsanto/Elei-oes-2026")
    group.add_argument("--snapshot-file", type=Path, help="Snapshot já calculado; regenera apenas artefatos")
    parser.add_argument("--output", type=Path, default=Path("."), help="Raiz do repositório Analise-eleitoral")
    parser.add_argument("--date", dest="snapshot_date", help="Data analítica YYYY-MM-DD")
    args = parser.parse_args()

    output = args.output.resolve()
    if args.snapshot_file:
        snapshot = json.loads(args.snapshot_file.read_text(encoding="utf-8"))
    else:
        snapshot_day = date.fromisoformat(args.snapshot_date) if args.snapshot_date else date.today()
        snapshot = build_snapshot(args.source.resolve(), snapshot_day)
        governance_path = output / "config" / "governance.json"
        governance = json.loads(governance_path.read_text(encoding="utf-8"))
        gate = publication_gate(snapshot, governance)
        snapshot.setdefault("qualidade", {})["publication_gate"] = gate
        if not gate["ok"]:
            quarantine = quarantine_snapshot(snapshot, output, gate)
            print(f"Snapshot reprovado e colocado em quarentena: {quarantine}")
            print("Motivos: " + "; ".join(gate["reasons"]))
            return 2
        write_snapshot_bundle(snapshot, output)

    chart_dir = output / "assets" / "charts"
    build_all_charts(snapshot, chart_dir)

    report_name = f"{snapshot['meta']['snapshot_date']}-relatorio-v{snapshot['meta']['pipeline_version']}.md"
    write_report(snapshot, output / "docs" / "reports" / report_name)
    write_report(snapshot, output / "docs" / "reports" / "latest.md")

    build_presentation(snapshot, chart_dir, output / "presentations" / "briefing-executivo-latest.pptx")
    dated = output / "presentations" / f"briefing-executivo-{snapshot['meta']['snapshot_date']}-v{snapshot['meta']['pipeline_version']}.pptx"
    if not dated.exists():
        build_presentation(snapshot, chart_dir, dated)

    write_release_manifest(snapshot, output)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
