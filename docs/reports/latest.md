# Relatório analítico — Eleições 2026

**Versão do pipeline:** 0.3.1  
**Snapshot:** 2026-09-05  
**Natureza:** análise descritiva, apartidária e reprodutível.

> Ausência de informação não é interpretada automaticamente como zero ou irregularidade.

## Sumário executivo

O catálogo reúne **20,000 registros de candidatura**. A camada financeira agrega **R$ 3.477.418.529,19** em receitas e **R$ 364.858.409,72** em despesas contratadas.

## Candidaturas por cargo

| Cargo | Registros | Participação |
|---|---:|---:|
| Deputado Estadual/Distrital | 11,691 | 58.45% |
| Deputado Federal | 7,778 | 38.89% |
| Senador | 319 | 1.59% |
| Governador | 199 | 0.99% |
| Presidente | 13 | 0.07% |

## Qualidade e freshness

- Gate de publicação: **APROVADO**.
- Cobertura federal: **27/27 UFs**.
- candidaturas: 0.417 h de idade; SLA 12 h; OK.
- financas: 13.153 h de idade; SLA 18 h; OK.
- camara: 24.318 h de idade; SLA 36 h; OK.

## Proveniência

Fonte: `MSsanto/Elei-oes-2026` · branch `main` · commit `ea0b1efbffc5fb211c60b3864b902b8e710774bd`.

Metodologia: `docs/METODOLOGIA.md`. Dicionário: `docs/DICIONARIO_METRICAS.md`.
