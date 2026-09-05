# Versionamento

O projeto usa três relógios independentes.

## Software — SemVer

Arquivo canônico: `VERSION`.

- MAJOR: mudança incompatível de schema, metodologia ou semântica publicada.
- MINOR: nova análise, fonte, automação ou capacidade sem quebra.
- PATCH: correção compatível, documentação, testes ou robustez.

## Schema analítico

Campo `meta.analysis_schema_version` no snapshot. Incrementar quando consumidores não puderem interpretar o novo formato sem adaptação.

## Release de dados

Arquivo `data/derived/release-manifest.json`. ID no padrão `YYYYMMDDTHHMMSSZ-schemaN-vX.Y.Z`, com commit/timestamps da fonte, hashes SHA-256 e estado dos controles de qualidade.

Atualização de dados não exige bump do software. Mudança de fórmula deve atualizar changelog, dicionário de métricas, versão quando aplicável, schema se incompatível e ADR quando houver decisão metodológica relevante.

Snapshots históricos são imutáveis por padrão. Correções excepcionais exigem incidente e novo release de dados.
