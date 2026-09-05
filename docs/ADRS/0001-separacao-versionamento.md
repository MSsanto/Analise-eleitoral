# ADR-0001 — Separar versão de software, schema e release de dados

**Status:** Aceito  
**Data:** 2026-09-05  
**Backlog:** AE-GOV-001, AE-REL-001

## Contexto

Dados mudam várias vezes ao dia, enquanto código e metodologia mudam em outra cadência. Uma única versão impediria distinguir atualização de dados de mudança analítica.

## Decisão

Adotar três identificadores independentes: SemVer para software; inteiro para `analysis_schema_version`; `data_release_id` temporal com hashes para cada release de dados.

## Consequências

Atualizações de dados não forçam bump do software; mudanças incompatíveis ficam explícitas; um número pode ser reproduzido pela combinação commit da fonte + versão do pipeline + schema + hash do snapshot.
