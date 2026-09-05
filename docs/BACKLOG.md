# Backlog canônico

Este arquivo é a **fonte canônica de trabalho** do `Analise-eleitoral`. Toda mudança relevante deve estar associada a um item do backlog, Issue ou ADR.

## Convenções

**Status**
- ✅ `CONCLUÍDO` — entregue na `main`, validado e documentado.
- 🚧 `EM ANDAMENTO` — implementação ou validação ativa.
- 📋 `BACKLOG` — aprovado, ainda não iniciado.
- 🔎 `PESQUISA` — depende de validação de fonte, método ou arquitetura.
- ⛔ `BLOQUEADO` — impedimento externo ou técnico documentado.
- 🧊 `SUSPENSO` — preservado historicamente, fora da prioridade atual.

**Prioridade**
- `P0` — integridade, rastreabilidade ou publicação incorreta; interrompe release.
- `P1` — necessário para confiabilidade operacional ou próxima versão.
- `P2` — ganho relevante de análise, automação ou UX de dados.
- `P3` — melhoria incremental ou dívida técnica não urgente.

**ID**: `AE-<workstream>-NNN`, por exemplo `AE-DQ-001`.

## Quadro atual

| ID | Prioridade | Status | Workstream | Entrega | Critério de aceite |
|---|---|---|---|---|---|
| AE-GOV-001 | P0 | ✅ CONCLUÍDO | Governança | Backlog canônico, versionamento e gates | Documentos exigidos e verificação automática presentes |
| AE-REL-001 | P0 | ✅ CONCLUÍDO | Releases | Manifesto de release de dados com SHA-256 | `data/derived/release-manifest.json` gerado e validado |
| AE-DQ-001 | P0 | ✅ CONCLUÍDO | Qualidade | Gates mínimos de integridade e artefatos | CI falha diante de artefato obrigatório ausente/inválido |
| AE-LIN-001 | P0 | ✅ CONCLUÍDO | Linhagem | Proveniência formal do repositório-fonte | Snapshot registra commit/timestamps de origem quando disponível |
| AE-PIPE-001 | P0 | ✅ CONCLUÍDO | Pipeline | Publicar pipeline analítico completo | Código, testes, configs e artefatos operacionais disponíveis na `main` |
| AE-DOC-001 | P0 | ✅ CONCLUÍDO | Documentação | Manual de utilização | Instalação, execução, interpretação, falhas e operação documentadas |
| AE-CI-001 | P0 | ✅ CONCLUÍDO | CI/CD | Pipeline automatizado com gates | Workflow executa análise, testes e publicação somente quando aprovado |
| AE-DQ-002 | P0 | ✅ CONCLUÍDO | Qualidade | Freshness gate por fonte | SLA configurável impede publicação de snapshot excessivamente defasado |
| AE-DQ-003 | P0 | ✅ CONCLUÍDO | Qualidade | Quarentena de snapshot inválido | Carga inválida não substitui `snapshot-latest.json` |
| AE-OPS-001 | P1 | ✅ CONCLUÍDO | Operação | Runbook, incidentes e rollback | Procedimento operacional documentado ponta a ponta |
| AE-REL-002 | P1 | ✅ CONCLUÍDO | Releases | SemVer + Conventional Commits + checklist | Regras publicadas e changelog atualizado |
| AE-DASH-001 | P1 | 🚧 EM ANDAMENTO | Dashboards | Visão executiva geral | KPIs de candidaturas, finanças, cobertura e freshness em uma única visão |
| AE-DASH-002 | P1 | 📋 BACKLOG | Dashboards | Visão financeira | Receitas, despesas, fontes, categorias, concentração e cobertura com filtros |
| AE-DASH-003 | P1 | 📋 BACKLOG | Dashboards | Visão de candidaturas | Cargo, UF, partido, gênero, cor/raça, escolaridade, idade e ocupação |
| AE-OBS-001 | P1 | 📋 BACKLOG | Observabilidade | Histórico de execuções e falhas | Registro de sucesso/falha, duração e causa raiz por execução |
| AE-ANA-001 | P1 | 📋 BACKLOG | Séries temporais | Delta diário/semanal de receitas e despesas | Comparação usa snapshots compatíveis e mesma versão de schema |
| AE-ANA-002 | P1 | 📋 BACKLOG | Séries temporais | Mudança de situação de candidatura | Eventos identificam valor anterior, novo valor e timestamp |
| AE-DATA-001 | P1 | 📋 BACKLOG | Dados | Catálogo de datasets legível por máquina | Cada dataset possui dono lógico, fonte, schema, SLA e política de retenção |
| AE-ID-001 | P1 | 🔎 PESQUISA | Identidade | Cobertura TSE ↔ Câmara | Métrica de vínculo com evidências, sem associação apenas por nome |
| AE-SEN-001 | P1 | ⛔ BLOQUEADO | Senado | Histórico senatorial | Fonte e regra de vínculo estabilizadas no repositório-fonte |
| AE-DASH-004 | P2 | 📋 BACKLOG | Dashboards | Visão territorial | UF e recortes territoriais com denominadores explícitos e sem inferências indevidas |
| AE-DASH-005 | P2 | 📋 BACKLOG | Dashboards | Visão temporal | Evolução de candidaturas e finanças entre snapshots compatíveis |
| AE-DASH-006 | P2 | 📋 BACKLOG | Dashboards | Saúde e qualidade dos dados | Cobertura, freshness, completude, inconsistências e status por dataset |
| AE-ANA-003 | P2 | 📋 BACKLOG | Diversidade | Gênero, cor/raça, escolaridade e idade por cargo/UF | Denominadores e ausências explícitos |
| AE-ANA-004 | P2 | 📋 BACKLOG | Finanças | Evolução da cobertura financeira | Cobertura por cargo, UF e partido com definição estável |
| AE-ANA-005 | P2 | 📋 BACKLOG | Finanças | Concentração de categorias de despesas | HHI/Top-N apenas em nível agregado e metodologia documentada |
| AE-PRIV-001 | P2 | 📋 BACKLOG | Privacidade | Auditoria de campos derivados | Nenhum artefato analítico reintroduz dado sensível reduzido na fonte |
| AE-REL-003 | P2 | ✅ CONCLUÍDO | Releases | Tags, GitHub Releases e pacote analítico automatizados | `v0.3.1` publicada com pacote ZIP validado via GitHub Actions |
| AE-OPS-002 | P2 | 📋 BACKLOG | Operação | Relatório de saúde semanal | Cobertura, freshness, falhas e divergências resumidas automaticamente |
| AE-ADR-001 | P2 | ✅ CONCLUÍDO | Arquitetura | Registro de decisões (ADR) | Diretório de ADRs e decisão inicial versionados |
| AE-TEST-001 | P2 | 📋 BACKLOG | Testes | Testes de regressão de métricas-chave | Fixtures congeladas detectam mudança não intencional |
| AE-PERF-001 | P3 | 📋 BACKLOG | Performance | Benchmark do pipeline | Tempo/memória registrados para baseline e regressão |

## Regras de movimentação

1. Item entra como `PESQUISA` quando a fonte ou o método ainda não são suficientemente confiáveis.
2. Só entra em `EM ANDAMENTO` quando há critério de aceite claro.
3. Só vira `CONCLUÍDO` após merge na `main`, testes, documentação e artefatos válidos.
4. Mudança de prioridade deve ser registrada no mesmo PR/commit do backlog.
5. Um item `P0` bloqueia release enquanto permanecer aberto e afetar a integridade do produto.
6. Trabalho não previsto que altere métrica, schema, fonte ou política de publicação deve ganhar ID antes do merge.

## Próxima janela recomendada — v0.4.0

Foco: **visões analíticas, observabilidade e comparabilidade temporal**.

1. AE-DASH-001 — dashboard executivo geral.
2. AE-DASH-002 — dashboard financeiro.
3. AE-DASH-003 — dashboard de candidaturas.
4. AE-OBS-001 — observabilidade das execuções.
5. AE-ANA-001 — séries temporais compatíveis.
6. AE-ANA-002 — radar de alterações de candidatura.
7. AE-DATA-001 — catálogo de datasets legível por máquina.

## Janela seguinte — v0.5.0

Foco: **aprofundamento analítico e qualidade visual**.

- AE-DASH-004 — visão territorial.
- AE-DASH-005 — visão temporal.
- AE-DASH-006 — saúde e qualidade dos dados.
- AE-ANA-003/004/005 — diversidade, cobertura financeira e concentração agregada.
