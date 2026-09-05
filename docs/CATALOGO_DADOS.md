# Catálogo de dados

| Dataset | Tipo | Fonte lógica | Saída principal | Frequência | SLA de freshness | Retenção |
|---|---|---|---|---|---|---|
| Candidaturas | origem normalizada | `Elei-oes-2026` / TSE | `snapshot-latest.json:candidaturas` | até 4x/dia | 12 h | histórico diário |
| Finanças eleitorais | origem normalizada | `Elei-oes-2026` / TSE | `snapshot-latest.json:financas` | até 2x/dia na origem | 18 h | histórico diário |
| Câmara | origem normalizada | `Elei-oes-2026` / Câmara | `snapshot-latest.json:qualidade` + futuras métricas | diária | 36 h | histórico diário |
| Candidaturas por cargo | derivado | snapshot | `candidaturas_por_cargo.csv` | a cada pipeline | acompanha snapshot | regenerável |
| Estadual por UF | derivado | snapshot | `deputado_estadual_por_uf.csv` | a cada pipeline | acompanha snapshot | regenerável |
| Receitas por fonte | derivado | snapshot | `receitas_por_fonte.csv` | a cada pipeline | acompanha snapshot | regenerável |
| Despesas por categoria | derivado | snapshot | `despesas_por_categoria.csv` | a cada pipeline | acompanha snapshot | regenerável |
| Relatório | produto | snapshot | `docs/reports/latest.md` | a cada pipeline | acompanha snapshot | versões datadas |
| Apresentação | produto | snapshot | `presentations/briefing-executivo-latest.pptx` | a cada pipeline | acompanha snapshot | versões datadas |

## Classificação

- **Origem normalizada**: dado já processado pelo repositório-fonte.
- **Derivado**: resultado matemático reproduzível deste repositório.
- **Produto**: artefato editorial/visual gerado a partir de derivados.

## Dono lógico

Enquanto o projeto tiver um único mantenedor, o responsável técnico é o owner do repositório. O ownership pode ser formalizado por domínio no `CODEOWNERS` quando houver novos contribuidores.
