# Runbook operacional

## Fluxo normal

1. Checkout dos dois repositórios em commits conhecidos.
2. Instalar dependências.
3. Executar pipeline.
4. Rodar testes.
5. Rodar gate de governança.
6. Validar outputs.
7. Gerar manifesto de release.
8. Publicar `data:` somente se tudo estiver válido.

## Falhas críticas

Totais divergentes do manifest são P0 e bloqueiam publicação. Fonte defasada deve ser marcada como freshness degradado. Despesas pagas iguais a zero são estado da carga, não prova de ausência de pagamentos. Histórico DDD sem vínculos não deve ser usado como evidência territorial.

## Rollback de dados

Identificar último snapshot validado, registrar incidente, restaurar `snapshot-latest.json`, preservar o snapshot problemático para auditoria, regenerar artefatos, criar novo manifesto e documentar causa/prevenção.

## GitHub Actions

Falha deve ser reproduzida localmente. Mudança de código passa por branch/PR. Não forçar push de dados que falharam em qualquer gate.
