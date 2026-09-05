# Manual de utilização — Análise Eleitoral 2026

## 1. Objetivo

Este repositório transforma os dados normalizados de `MSsanto/Elei-oes-2026` em estatísticas, séries derivadas, relatórios, gráficos e apresentações auditáveis. Ele não substitui a fonte oficial nem o repositório de coleta.

## 2. Públicos

- **Leitor/analista:** consulta relatórios, CSVs, gráficos e apresentações.
- **Mantenedor:** executa o pipeline, valida dados e trata incidentes.
- **Desenvolvedor:** altera métricas, schemas, testes e automações.

## 3. Estrutura principal

- `data/derived/` — snapshots e tabelas derivadas publicáveis.
- `data/derived/history/` — snapshots históricos aprovados.
- `data/quarantine/` — cargas reprovadas; nunca são promovidas automaticamente.
- `assets/charts/` — gráficos gerados.
- `docs/reports/` — relatórios analíticos.
- `presentations/` — briefing executivo.
- `src/analise_eleitoral/` — código analítico.
- `config/governance.json` — SLAs e regras de governança.

## 4. Instalação local

Requer Python 3.13+ e um checkout local do repositório-fonte.

```bash
python -m venv .venv
source .venv/bin/activate  # Linux/macOS
# .venv\\Scripts\\activate  # Windows
python -m pip install --upgrade pip
python -m pip install -r requirements.txt -r requirements-dev.txt -e .
```

## 5. Executar o pipeline

```bash
python scripts/run_analysis.py --source ../Elei-oes-2026 --output .
```

Fluxo: carregar fonte → calcular snapshot candidato → validar integridade → validar freshness → publicar ou quarentenar → gerar gráficos → relatório → apresentação → manifesto de release.

Código de saída `0` indica publicação válida. Código `2` indica snapshot reprovado e preservado em `data/quarantine/`; nesse caso o `snapshot-latest.json` anterior permanece intacto.

## 6. Freshness gate

Os limites são definidos em `config/governance.json`. O pipeline compara os timestamps das fontes com os SLAs por família. Timestamp ausente, inválido ou acima do SLA reprova a publicação.

Ajustar SLA é uma mudança de governança e deve ter item de backlog/Issue e justificativa no commit ou ADR.

## 7. Quarentena

Quando um gate falha:

1. o novo snapshot **não** substitui `data/derived/snapshot-latest.json`;
2. a carga é gravada em `data/quarantine/` com o diagnóstico;
3. o workflow falha;
4. o mantenedor corrige a fonte ou a regra e executa novamente;
5. nunca copie manualmente um arquivo de quarentena para `derived/` sem nova validação.

## 8. Validação antes de release

```bash
pytest -q
python scripts/check_governance.py
python scripts/validate_outputs.py
```

Todos os comandos devem passar. Falha em P0 bloqueia release.

## 9. Interpretação dos dados

- `0` é valor observado somente quando a fonte realmente informa zero.
- ausência de campo não deve ser convertida automaticamente em zero.
- falta de cobertura deve aparecer como limitação de dados.
- rankings ou notas políticas não fazem parte da política do projeto.
- mudanças de metodologia exigem versionamento e documentação.

## 10. Atualização automática

`.github/workflows/analise-eleitoral.yml` roda após as janelas regulares da fonte. Só commita derivados quando todos os gates passam. Carga inválida permanece em quarentena no runner e a execução termina com erro para evitar publicação silenciosa.

## 11. Versionamento

- `VERSION`: versão do software via SemVer.
- `analysis_schema_version`: versão lógica do schema analítico.
- `data_release_id`: identifica a execução/snapshot de dados.

Uma nova coleta não implica nova versão do software.

## 12. Falhas e incidentes

Consulte `docs/RUNBOOK.md` e `docs/INCIDENTES.md`. Para erro de fonte desatualizada, primeiro valide o timestamp no repositório-fonte. Para divergência de contagem, compare `manifest_checks` no snapshot candidato. Não force publicação para “destravar” o pipeline.

## 13. Desenvolvimento de nova métrica

Antes do merge: criar ID `AE-*`, definir denominador e ausências, escrever teste, documentar no dicionário/metodologia, rodar gates e atualizar changelog quando aplicável.
