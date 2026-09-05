# Análise Eleitoral 2026

Camada analítica, documental e visual baseada no repositório `MSsanto/Elei-oes-2026`.

**Versão atual:** `0.2.0`

## Controle do projeto

O repositório separa três dimensões: versão do software (SemVer), versão do schema analítico e release temporal dos dados. O backlog canônico usa IDs `AE-*` e prioridades P0–P3.

Documentos centrais:

- `docs/BACKLOG.md` — prioridades e estado do trabalho;
- `docs/VERSIONAMENTO.md` — SemVer, schema e releases de dados;
- `docs/CONTROLE_DE_RELEASES.md` — gates, commits, branches e rollback;
- `docs/LINHAGEM_DADOS.md` — rastreabilidade ponta a ponta;
- `docs/RUNBOOK.md` — operação e recuperação;
- `docs/INCIDENTES.md` — severidade e causa raiz;
- `docs/RETENCAO_E_SNAPSHOTS.md` — imutabilidade e retenção;
- `docs/ADRS/` — decisões arquiteturais e metodológicas.

## Gates de publicação

Um release válido exige testes, verificação de governança, validação dos outputs, proveniência do snapshot, manifesto SHA-256 e ausência de P0 aplicável em aberto. Atualizações automáticas de dados não alteram a versão do software por si só.

## Princípios

Fontes oficiais, rastreabilidade, mesma regra de cálculo para todos, nenhuma nota/recomendação de candidato, ausência de informação não tratada automaticamente como zero ou irregularidade e toda mudança metodológica versionada.
