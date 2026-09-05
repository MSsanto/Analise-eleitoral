from __future__ import annotations
from pathlib import Path
from typing import Any


def _brl(value: float) -> str:
    return f"R$ {value:,.2f}".replace(',', 'X').replace('.', ',').replace('X', '.')


def write_report(snapshot: dict[str, Any], path: Path) -> None:
    m=snapshot['meta']; c=snapshot['candidaturas']; f=snapshot['financas']; q=snapshot['qualidade']
    lines=['# Relatório analítico — Eleições 2026','',f"**Versão do pipeline:** {m['pipeline_version']}  ",f"**Snapshot:** {m['snapshot_date']}  ",'**Natureza:** análise descritiva, apartidária e reprodutível.','','> Ausência de informação não é interpretada automaticamente como zero ou irregularidade.','','## Sumário executivo','',f"O catálogo reúne **{c['candidaturas_total']:,} registros de candidatura**. A camada financeira agrega **{_brl(f['total_receitas'])}** em receitas e **{_brl(f['total_despesas_contratadas'])}** em despesas contratadas.",'','## Candidaturas por cargo','','| Cargo | Registros | Participação |','|---|---:|---:|']
    lines += [f"| {r['categoria']} | {r['total']:,} | {r['percentual']:.2f}% |" for r in c['candidaturas_por_cargo']]
    lines += ['','## Qualidade e freshness','']; gate=q.get('publication_gate',{}); lines += [f"- Gate de publicação: **{'APROVADO' if gate.get('ok') else 'NÃO REGISTRADO/REPROVADO'}**.",f"- Cobertura federal: **{q.get('federal_ufs_presentes',0)}/{q.get('federal_ufs_esperadas',0)} UFs**."]
    for name,row in (gate.get('freshness',{}).get('sources',{}) or {}).items(): lines.append(f"- {name}: {row.get('age_hours')} h de idade; SLA {row.get('sla_hours')} h; {'OK' if row.get('ok') else 'FALHA'}.")
    lines += ['','## Proveniência','',f"Fonte: `{m.get('source_repository')}` · branch `{m.get('source_branch')}` · commit `{m.get('source_commit') or 'não registrado no baseline'}`.",'','Metodologia: `docs/METODOLOGIA.md`. Dicionário: `docs/DICIONARIO_METRICAS.md`.']
    path.parent.mkdir(parents=True,exist_ok=True); path.write_text('\n'.join(lines)+'\n',encoding='utf-8')
