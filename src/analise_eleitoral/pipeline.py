from __future__ import annotations

from datetime import date, datetime, timezone
from pathlib import Path
from typing import Any
import subprocess

from . import __version__
from .io import iter_finance_records, load_candidates, load_source_metadata, write_json
from .metrics import candidate_metrics, finance_metrics


def _iso_now() -> str: return datetime.now(timezone.utc).isoformat()

def _git_commit(repo_root: Path) -> str | None:
    try:
        proc=subprocess.run(["git","-C",str(repo_root),"rev-parse","HEAD"],capture_output=True,text=True,check=True,timeout=5)
        return proc.stdout.strip() or None
    except (OSError, subprocess.SubprocessError): return None


def build_snapshot(source_root: Path, snapshot_date: date | None = None) -> dict[str, Any]:
    snapshot_date=snapshot_date or date.today(); records,expected=load_candidates(source_root); source_meta=load_source_metadata(source_root); candidate=candidate_metrics(records,snapshot_date); finance=finance_metrics(records,source_meta.get("finance_overview"),iter_finance_records(source_root))
    state_rows=candidate.get("por_cargo",{}).get("Deputado Estadual/Distrital",{}).get("uf",[]); state_rows=[{"uf":r["categoria"],"categoria":r["categoria"],"total":r["total"],"percentual":r["percentual"]} for r in state_rows if r.get("categoria") not in ("BR","NÃO INFORMADO")]; state_rows=sorted(state_rows,key=lambda r:(-r["total"],r["uf"]))
    pres=candidate.get("por_cargo",{}).get("Presidente",{}); presidency={"total":pres.get("total",0),"genero":pres.get("genero",[]),"cor_raca":pres.get("cor_raca",[]),"grau_instrucao":pres.get("grau_instrucao",[]),"ocupacao":pres.get("ocupacao",[]),"idade":pres.get("idade",{})}
    cand_manifest=source_meta.get("candidate_manifest",{}); federal_meta=source_meta.get("federal_metadata",{}); finance_manifest=source_meta.get("finance_manifest",{}); camara_meta=source_meta.get("camara_metadata",{}); radar=source_meta.get("radar",{})
    actual={r["categoria"]:int(r["total"]) for r in candidate["candidaturas_por_cargo"]}; manifest_checks={office:{"esperado":int(total),"lido":int(actual.get(office,0)),"ok":int(total)==int(actual.get(office,0))} for office,total in expected.items()}
    source_generated={"candidaturas":cand_manifest.get("generated_at_utc") or federal_meta.get("generated_at_utc"),"financas":finance_manifest.get("generated_at_utc") or (source_meta.get("finance_overview") or {}).get("generated_at_utc"),"camara":camara_meta.get("generated_at_utc")}
    return {"meta":{"analysis_schema_version":1,"pipeline_version":__version__,"generated_at_utc":_iso_now(),"snapshot_date":snapshot_date.isoformat(),"source_repository":"MSsanto/Elei-oes-2026","source_branch":"main","source_commit":_git_commit(source_root),"source_generated_at_utc":source_generated},"candidaturas":candidate,"financas":finance,"recortes":{"deputado_estadual_por_uf":state_rows,"deputado_estadual_top3_percentual":round(sum(float(r.get("percentual",0)) for r in state_rows[:3]),4),"deputado_estadual_top10_percentual":round(sum(float(r.get("percentual",0)) for r in state_rows[:10]),4),"presidencia":presidency},"qualidade":{"manifest_checks":manifest_checks,"federal_ufs_presentes":int(federal_meta.get("ufs_with_records") or len(federal_meta.get("ufs_present",[]))),"federal_ufs_esperadas":len(federal_meta.get("ufs_expected",[])),"ddd_historico_confirmados":int((federal_meta.get("regionalizacao_historica") or {}).get("candidaturas_com_historico_confirmado") or 0),"ddd_principal_confirmados":int((federal_meta.get("regionalizacao_historica") or {}).get("candidaturas_com_ddd_principal") or 0),"camara_registros_historicos":int(camara_meta.get("records") or 0),"historico_senado":((cand_manifest.get("cargos") or {}).get("senador") or {}).get("historico_senado","não informado"),"radar_mode":radar.get("mode","não informado"),"radar_events":len(radar.get("events",[]) or []),"alertas":["total_despesas_pagas igual a zero deve ser tratado como estado da carga, não como prova de ausência de pagamentos" if finance.get("total_despesas_pagas")==0 else None,"regionalização histórica por DDD sem vínculos confirmados; não usar para interpretação territorial" if int((federal_meta.get("regionalizacao_historica") or {}).get("candidaturas_com_historico_confirmado") or 0)==0 else None]}}


def write_snapshot_bundle(snapshot: dict[str, Any], output_root: Path) -> None:
    import csv
    latest=output_root/"data"/"derived"/"snapshot-latest.json"; history=output_root/"data"/"derived"/"history"/f"{snapshot['meta']['snapshot_date']}.json"; write_json(latest,snapshot); write_json(history,snapshot); derived=output_root/"data"/"derived"; derived.mkdir(parents=True,exist_ok=True)
    def write_csv(path,header,rows):
        with path.open("w",encoding="utf-8",newline="") as fh:
            w=csv.writer(fh); w.writerow(header); w.writerows(rows)
    write_csv(derived/"candidaturas_por_cargo.csv",["cargo","total","percentual"],[[r["categoria"],r["total"],r["percentual"]] for r in snapshot["candidaturas"]["candidaturas_por_cargo"]])
    write_csv(derived/"deputado_estadual_por_uf.csv",["uf","total","percentual_no_cargo"],[[r["categoria"],r["total"],r["percentual"]] for r in snapshot["recortes"]["deputado_estadual_por_uf"]])
    write_csv(derived/"receitas_por_fonte.csv",["fonte","valor","percentual"],[[r["categoria"],r["valor"],r["percentual"]] for r in snapshot["financas"]["receitas_por_fonte"]])
    write_csv(derived/"despesas_por_categoria.csv",["categoria","valor","percentual"],[[r["categoria"],r["valor"],r["percentual"]] for r in snapshot["financas"]["despesas_por_categoria"]])
