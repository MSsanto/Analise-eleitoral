# Análise Eleitoral 2026

Camada analítica, documental e visual baseada no repositório `MSsanto/Elei-oes-2026`.

**Versão atual:** `0.3.0`

## Estado atual

As prioridades P0 de governança, publicação, qualidade e operação estão implementadas. O pipeline possui freshness gate por fonte, quarentena para snapshots inválidos, CI/CD, testes e documentação operacional.

## Controle do projeto

O repositório separa três dimensões: versão do software (SemVer), versão do schema analítico e release temporal dos dados. O backlog canônico usa IDs `AE-*` e prioridades P0–P3.

Documentos centrais:

- `docs/BACKLOG.md` — prioridades e estado do trabalho;
- `docs/MANUAL_DE_UTILIZACAO.md` — instalação, execução, interpretação e tratamento de falhas;
- `docs/VERSIONAMENTO.md` — SemVer, schema e releases de dados;
- `docs/CONTROLE_DE_RELEASES.md` — gates, commits, branches e rollback;
- `docs/LINHAGEM_DADOS.md` — rastreabilidade ponta a ponta;
- `docs/RUNBOOK.md` — operação e recuperação;
- `docs/INCIDENTES.md` — severidade e causa raiz;
- `docs/RETENCAO_E_SNAPSHOTS.md` — imutabilidade e retenção;
- `docs/ADRS/` — decisões arquiteturais e metodológicas.

## Gates de publicação

Um release válido exige testes, verificação de governança, validação dos outputs, integridade do snapshot, freshness dentro do SLA e manifesto SHA-256. Snapshot reprovado é enviado à quarentena e nunca substitui automaticamente o último `snapshot-latest.json` válido.

## Princípios

Fontes oficiais, rastreabilidade, mesma regra de cálculo para todos, nenhuma nota/recomendação de candidato, ausência de informação não tratada automaticamente como zero ou irregularidade e toda mudança metodológica versionada.
