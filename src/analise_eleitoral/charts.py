from __future__ import annotations
from pathlib import Path
from typing import Any
import matplotlib.pyplot as plt


def _bar(rows: list[dict[str, Any]], path: Path, title: str, label_key: str = 'categoria', value_key: str = 'total', top: int | None = None) -> None:
    data = rows[:top] if top else rows
    labels = [str(r.get(label_key, '')) for r in data]
    values = [float(r.get(value_key, 0) or 0) for r in data]
    fig, ax = plt.subplots(figsize=(10, 5.5)); ax.barh(labels[::-1], values[::-1]); ax.set_title(title); ax.grid(axis='x', alpha=.2); fig.tight_layout(); path.parent.mkdir(parents=True, exist_ok=True); fig.savefig(path, dpi=160, bbox_inches='tight'); plt.close(fig)


def build_all_charts(snapshot: dict[str, Any], out_dir: Path) -> None:
    out_dir.mkdir(parents=True, exist_ok=True)
    specs=[('candidaturas_por_cargo',snapshot['candidaturas']['candidaturas_por_cargo'],'Candidaturas por cargo','categoria','total',None),('deputados_estaduais_top_ufs',snapshot['recortes']['deputado_estadual_por_uf'],'Deputado Estadual/Distrital — maiores UFs','categoria','total',15),('receitas_por_fonte',snapshot['financas']['receitas_por_fonte'],'Receitas por fonte','categoria','valor',None),('despesas_top10',snapshot['financas']['despesas_por_categoria'],'Despesas contratadas — top 10 categorias','categoria','valor',10)]
    for name,rows,title,lk,vk,top in specs:
        _bar(rows,out_dir/f'{name}.png',title,lk,vk,top); _bar(rows,out_dir/f'{name}.svg',title,lk,vk,top)
