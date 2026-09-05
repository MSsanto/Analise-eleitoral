# Changelog

O projeto usa versionamento semântico para o código da camada analítica. Os snapshots e releases de dados têm identidade própria e podem mudar sem alterar a versão do software.

## [0.3.0] - 2026-09-05

### Added
- Freshness gate configurável por fonte.
- Quarentena de snapshots reprovados sem sobrescrever o último snapshot válido.
- Manual de utilização oficial.
- Testes de qualidade temporal e preservação do latest.
- Publicação do pipeline completo e CI/CD com gates de qualidade.

## [0.2.0] — 2026-09-05

### Adicionado
- Backlog canônico com IDs `AE-*`, prioridades P0–P3, status e critérios de aceite.
- Controle formal de releases com três dimensões: software, schema analítico e release de dados.
- Manifesto de release com SHA-256 dos principais artefatos.
- Linhagem de dados com commit do repositório-fonte quando disponível.
- Catálogo de dados, SLAs de freshness e política de retenção.
- Runbook operacional, rollback e gestão de incidentes.
- ADRs para decisões arquiteturais/metodológicas.
- Templates de Issue/PR e CODEOWNERS.
- Gate automático de governança e sincronização de versão.

### Alterado
- Pipeline passa a usar a versão do pacote em vez de versão fixa no código.
- CI passa a validar testes, governança e outputs antes de publicar derivados.

## [0.1.0] — 2026-09-05

### Adicionado
- Estrutura inicial do repositório analítico.
- Pipeline reprodutível para candidaturas, finanças, qualidade e proveniência.
- Snapshot basal de 05/09/2026.
- Gráficos em SVG/PNG e apresentação executiva em PPTX.
- Relatório metodológico e dicionário de métricas.
- Testes de métricas e validação de artefatos.
- GitHub Actions para atualizar a camada derivada após as janelas de coleta do repositório-fonte.

### Política editorial
- Nenhuma nota, selo, recomendação ou ranking de candidatos.
- Agregações descritivas são separadas de interpretações.
- Ausência de registro não é tratada como irregularidade.
