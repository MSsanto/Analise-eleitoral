# Análise Eleitoral 2026

Camada analítica reprodutível e apartidária para os dados públicos consolidados do projeto `MSsanto/Elei-oes-2026`.

**Versão atual:** `0.3.1`

## O que este repositório entrega

- snapshots analíticos versionados;
- métricas agregadas de candidaturas e finanças;
- relatórios, gráficos e apresentações;
- dashboards analíticos;
- controle de qualidade, freshness, linhagem e quarentena;
- releases versionadas com pacote ZIP validado.

## Dashboard executivo

O primeiro dashboard P1 está em `dashboard/index.html` e consome `data/derived/snapshot-latest.json` quando servido por HTTP/GitHub Pages.

## Controle do projeto

O repositório separa três dimensões: versão do software (SemVer), versão do schema analítico e release temporal dos dados. O backlog canônico usa IDs `AE-*` e prioridades P0–P3.

Documentos centrais:

- `docs/BACKLOG.md` — prioridades e estado do trabalho;
- `docs/MANUAL_DE_UTILIZACAO.md` — instalação, execução, interpretação e tratamento de falhas;
- `docs/VERSIONAMENTO.md` — SemVer, schema e releases de dados;
- `docs/CONTROLE_DE_RELEASES.md` — gates, commits, branches e rollback;
- `docs/LINHAGEM_DADOS.md` — rastreabilidade ponta a ponta;
- `docs/GOVERNANCA.md` — princípios e regras de publicação;
- `docs/QUALIDADE_DADOS.md` — controles e limites de interpretação;
- `docs/CATALOGO_DADOS.md` — catálogo humano dos datasets;
- `docs/ROADMAP.md` — evolução planejada;
- `docs/RUNBOOK.md` — operação e recuperação.

## Gates de publicação

Um release válido exige testes, verificação de governança, validação dos outputs, integridade do snapshot, freshness dentro do SLA e manifesto SHA-256. Snapshot reprovado é enviado à quarentena e nunca substitui automaticamente o último `snapshot-latest.json` válido.

## Release atual

A release oficial `v0.3.1` foi publicada via GitHub Actions com pacote analítico ZIP validado.

## Princípios

Fontes oficiais, rastreabilidade, mesma regra de cálculo para todos, nenhuma nota/recomendação de candidato, ausência de informação não tratada automaticamente como zero ou irregularidade e toda mudança metodológica versionada.
