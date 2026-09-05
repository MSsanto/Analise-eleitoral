# Linhagem de dados

Fluxo: fontes oficiais → `MSsanto/Elei-oes-2026` → commit/timestamps da fonte → `MSsanto/Analise-eleitoral` → métricas/controles → snapshot → CSV/gráficos/relatório/apresentação → manifesto SHA-256.

## Proveniência mínima por snapshot

- `analysis_schema_version`;
- `pipeline_version`;
- `generated_at_utc`;
- `snapshot_date`;
- `source_repository`;
- `source_branch`;
- `source_commit` quando disponível;
- timestamps de candidaturas, finanças e Câmara.

## Proveniência mínima por release

O `release-manifest.json` registra `data_release_id`, versão do software e schema, geração, commit da fonte, SHA-256 do snapshot e principais derivados e estado dos gates.

## Regra de publicação

Se não for possível determinar a origem ou a transformação de uma métrica, ela não é publicável como estatística consolidada.
