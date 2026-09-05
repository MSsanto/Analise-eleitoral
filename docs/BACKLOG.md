# Backlog canônico

Este arquivo é a fonte canônica de trabalho do `Analise-eleitoral`.

## Convenções

Status: `CONCLUÍDO`, `EM ANDAMENTO`, `BACKLOG`, `PESQUISA`, `BLOQUEADO`, `SUSPENSO`.

Prioridades: `P0` integridade/publicação; `P1` confiabilidade/próxima versão; `P2` ganho relevante; `P3` melhoria incremental.

IDs seguem `AE-<workstream>-NNN`.

## Quadro atual

| ID | Prioridade | Status | Workstream | Entrega |
|---|---|---|---|---|
| AE-GOV-001 | P0 | CONCLUÍDO | Governança | Backlog, versionamento e gates |
| AE-REL-001 | P0 | CONCLUÍDO | Releases | Manifesto de release com SHA-256 |
| AE-DQ-001 | P0 | CONCLUÍDO | Qualidade | Gates mínimos de integridade |
| AE-LIN-001 | P0 | CONCLUÍDO | Linhagem | Proveniência formal da fonte |
| AE-OPS-001 | P1 | CONCLUÍDO | Operação | Runbook, incidentes e rollback |
| AE-DQ-002 | P1 | BACKLOG | Qualidade | Freshness gate por fonte |
| AE-DQ-003 | P1 | BACKLOG | Qualidade | Quarentena de snapshot inválido |
| AE-OBS-001 | P1 | BACKLOG | Observabilidade | Histórico de execuções e falhas |
| AE-ANA-001 | P1 | BACKLOG | Séries temporais | Delta diário/semanal financeiro |
| AE-ANA-002 | P1 | BACKLOG | Séries temporais | Mudança de situação de candidatura |
| AE-DATA-001 | P1 | BACKLOG | Dados | Catálogo de datasets por máquina |
| AE-ID-001 | P1 | PESQUISA | Identidade | Cobertura TSE ↔ Câmara |
| AE-SEN-001 | P1 | BLOQUEADO | Senado | Histórico senatorial |
| AE-ANA-003 | P2 | BACKLOG | Diversidade | Perfil por cargo/UF/partido |
| AE-ANA-004 | P2 | BACKLOG | Finanças | Evolução da cobertura financeira |
| AE-REL-003 | P2 | BACKLOG | Releases | Tags e GitHub Releases automáticas |
| AE-OPS-002 | P2 | BACKLOG | Operação | Relatório de saúde semanal |
| AE-TEST-001 | P2 | BACKLOG | Testes | Regressão de métricas-chave |
| AE-PERF-001 | P3 | BACKLOG | Performance | Benchmark do pipeline |

## Regras

1. Trabalho que altera métrica, schema, fonte ou publicação recebe ID antes do merge.
2. Só entra em `EM ANDAMENTO` com critério de aceite objetivo.
3. Só vira `CONCLUÍDO` após merge na `main`, testes, documentação e artefatos válidos.
4. Mudança de prioridade é registrada no backlog/Issue.
5. P0 aplicável aberto bloqueia release.

## Próxima versão — v0.3.0

Foco: freshness gate, quarentena, observabilidade, séries temporais e testes de regressão.
