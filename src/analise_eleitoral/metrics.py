from __future__ import annotations

from collections import Counter, defaultdict
from datetime import date, datetime
from math import isfinite
from statistics import mean, median
from typing import Any, Iterable


def parse_tse_date(value: str | None) -> date | None:
    if not value:
        return None
    for fmt in ("%d/%m/%Y", "%Y-%m-%d"):
        try:
            return datetime.strptime(value, fmt).date()
        except (TypeError, ValueError):
            pass
    return None


def age_at(birth_date: date, snapshot_date: date) -> int:
    return snapshot_date.year - birth_date.year - ((snapshot_date.month, snapshot_date.day) < (birth_date.month, birth_date.day))


def age_bin(age: int | None) -> str:
    if age is None: return "não informado"
    if age < 30: return "<30"
    if age < 40: return "30-39"
    if age < 50: return "40-49"
    if age < 60: return "50-59"
    if age < 70: return "60-69"
    return "70+"


def distribution(values: Iterable[Any]) -> list[dict[str, Any]]:
    counts = Counter("NÃO INFORMADO" if v in (None, "") else str(v) for v in values)
    total = sum(counts.values())
    return [{"categoria": k, "total": v, "percentual": round((v / total * 100) if total else 0, 4)} for k, v in sorted(counts.items(), key=lambda kv: (-kv[1], kv[0]))]


def numeric_summary(values: Iterable[float]) -> dict[str, float | int | None]:
    data = sorted(float(v) for v in values if v is not None and isfinite(float(v)))
    if not data: return {"n": 0, "min": None, "mediana": None, "media": None, "max": None}
    return {"n": len(data), "min": round(data[0],4), "mediana": round(median(data),4), "media": round(mean(data),4), "max": round(data[-1],4)}


def percentile(values: Iterable[float], q: float) -> float | None:
    data = sorted(float(v) for v in values if v is not None and isfinite(float(v)))
    if not data: return None
    if len(data) == 1: return data[0]
    pos = (len(data)-1)*q; low=int(pos); high=min(low+1,len(data)-1); weight=pos-low
    return data[low]*(1-weight)+data[high]*weight


def gini(values: Iterable[float]) -> float | None:
    data = sorted(max(0.0,float(v)) for v in values if v is not None and isfinite(float(v)))
    n=len(data)
    if n==0: return None
    total=sum(data)
    if total==0: return 0.0
    weighted=sum((i+1)*v for i,v in enumerate(data))
    return (2*weighted)/(n*total)-(n+1)/n


def candidate_metrics(records: list[dict[str, Any]], snapshot_date: date) -> dict[str, Any]:
    ids=[str(r.get("id_tse","")) for r in records]
    ages=[]; age_groups=[]
    for r in records:
        dob=parse_tse_date(r.get("data_nascimento")); age=age_at(dob,snapshot_date) if dob else None
        if age is not None and 16 <= age <= 120: ages.append(age); age_groups.append(age_bin(age))
        else: age_groups.append("não informado")
    by_office: dict[str,list[dict[str,Any]]] = defaultdict(list)
    for r in records: by_office[r.get("cargo_analise","NÃO INFORMADO")].append(r)
    office_metrics={}
    for office,items in sorted(by_office.items()):
        office_ages=[]
        for item in items:
            dob=parse_tse_date(item.get("data_nascimento"))
            if dob:
                a=age_at(dob,snapshot_date)
                if 16 <= a <= 120: office_ages.append(a)
        office_metrics[office]={"total":len(items),"genero":distribution(i.get("genero") for i in items),"cor_raca":distribution(i.get("cor_raca") for i in items),"grau_instrucao":distribution(i.get("grau_instrucao") for i in items),"ocupacao":distribution(i.get("ocupacao") for i in items)[:20],"partido":distribution(i.get("partido") for i in items),"uf":distribution(i.get("uf") for i in items),"idade":numeric_summary(office_ages)}
    required=["id_tse","nome","partido","uf","genero","grau_instrucao","ocupacao"]
    total=len(records)
    completeness={f:{"presentes":sum(1 for r in records if r.get(f) not in (None,"","#NULO")),"total":total} for f in required}
    for row in completeness.values(): row["percentual"]=round((row["presentes"]/total*100) if total else 0,4)
    return {"candidaturas_total":total,"ids_duplicados":len(ids)-len(set(ids)),"candidaturas_por_cargo":distribution(r.get("cargo_analise") for r in records),"candidaturas_por_uf":distribution(r.get("uf") for r in records),"candidaturas_por_partido":distribution(r.get("partido") for r in records),"genero":distribution(r.get("genero") for r in records),"cor_raca":distribution(r.get("cor_raca") for r in records),"grau_instrucao":distribution(r.get("grau_instrucao") for r in records),"ocupacao_top20":distribution(r.get("ocupacao") for r in records)[:20],"idade":numeric_summary(ages),"faixa_etaria":distribution(age_groups),"por_cargo":office_metrics,"completude":completeness}


def finance_metrics(records: list[dict[str, Any]], overview: dict[str, Any] | None, finance_records: Iterable[dict[str, Any]]) -> dict[str, Any]:
    overview=overview or {}; candidate_by_id={str(r.get("id_tse")):r for r in records if r.get("id_tse")}; matched=0; unmatched=0; receipts=[]; contracted=[]
    by_office=defaultdict(lambda:{"registros":0,"receitas":0.0,"despesas_contratadas":0.0}); by_uf=defaultdict(lambda:{"registros":0,"receitas":0.0,"despesas_contratadas":0.0})
    for fin in finance_records:
        c=candidate_by_id.get(str(fin.get("id_tse","")))
        if c is None: unmatched += 1; continue
        matched += 1; summary=fin.get("resumo",{}) or {}; rec=float(summary.get("total_receitas") or 0); exp=float(summary.get("total_despesas_contratadas") or 0); receipts.append(rec); contracted.append(exp)
        for bucket,key in ((by_office,c.get("cargo_analise","NÃO INFORMADO")),(by_uf,c.get("uf","NÃO INFORMADO"))): bucket[key]["registros"] += 1; bucket[key]["receitas"] += rec; bucket[key]["despesas_contratadas"] += exp
    total_receipts=float(overview.get("total_receitas") or 0); total_expenses=float(overview.get("total_despesas_contratadas") or 0)
    def add_share(items,den):
        out=[]
        for row in items or []:
            item=dict(row); value=float(row.get("valor") or 0); item["percentual"]=round((value/den*100) if den else 0,4); out.append(item)
        return sorted(out,key=lambda r:float(r.get("valor") or 0),reverse=True)
    categories=add_share(overview.get("despesas_por_categoria",[]),total_expenses); sources=add_share(overview.get("receitas_por_fonte",[]),total_receipts); origins=add_share(overview.get("receitas_por_origem",[]),total_receipts)
    top10=sum(float(x.get("valor") or 0) for x in categories[:10])/total_expenses*100 if total_expenses else 0
    return {"total_receitas":total_receipts,"total_despesas_contratadas":total_expenses,"total_despesas_pagas":float(overview.get("total_despesas_pagas") or 0),"candidaturas_com_financas_fonte":int(overview.get("candidaturas_com_financas") or 0),"registros_financeiros_vinculados_catalogo":matched,"registros_financeiros_sem_vinculo_catalogo":unmatched,"cobertura_financeira_catalogo_percentual":round((matched/len(candidate_by_id)*100) if candidate_by_id else 0,4),"despesas_contratadas_sobre_receitas_percentual":round((total_expenses/total_receipts*100) if total_receipts else 0,4),"receitas_por_fonte":sources,"receitas_por_origem":origins,"despesas_por_categoria":categories,"concentracao_top10_despesas_percentual":round(top10,4),"distribuicao_por_cargo":dict(by_office),"distribuicao_por_uf":dict(by_uf),"receitas_por_candidatura":{"n":len(receipts),"mediana":round(percentile(receipts,.5) or 0,2),"p90":round(percentile(receipts,.9) or 0,2),"gini":round(gini(receipts) or 0,4)},"despesas_por_candidatura":{"n":len(contracted),"mediana":round(percentile(contracted,.5) or 0,2),"p90":round(percentile(contracted,.9) or 0,2),"gini":round(gini(contracted) or 0,4)},"fornecedores_registros":int((overview.get("fornecedores") or {}).get("records") or 0)}
