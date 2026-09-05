# Governança analítica

## Princípios

A camada analítica é factual, apartidária e reprodutível. Ela não atribui nota, confiabilidade, mérito, risco político ou recomendação eleitoral a pessoas, partidos ou candidaturas.

## Separação entre fato e derivação

Cada saída deve distinguir:
- **valor de origem**, publicado pela fonte oficial ou pelo repositório-fonte;
- **métrica derivada**, calculada por este repositório;
- **limitação**, quando a cobertura, a atualização ou o vínculo entre bases não permitem uma conclusão mais forte.

## Regras de publicação

- Não publicar rankings de candidatos por gasto, patrimônio, arrecadação ou qualquer escore composto como mecanismo editorial de julgamento.
- Comparações agregadas por cargo, UF, partido, categoria ou faixa são permitidas quando a definição estiver documentada.
- Não reproduzir listas individuais de doadores em artefatos derivados deste repositório.
- Não inferir irregularidade por ausência de dado, atraso de prestação ou valor igual a zero.
- Alterações metodológicas exigem changelog e versão.

## Auditoria

Todo snapshot inclui: repositório-fonte, branch, horários das bases, versão do pipeline, totais de entrada e controles de qualidade.

## Modelo operacional

- `docs/BACKLOG.md` é a fonte canônica de prioridades e estado.
- `config/governance.json` contém regras verificáveis por máquina.
- Releases passam por testes, gate de governança e validação de artefatos.
- Decisões metodológicas/arquiteturais relevantes usam ADR.
- Incidentes que alterem número publicado exigem registro e correção versionada.
- `snapshot-latest.json` só representa o último estado **validado**, nunca simplesmente a última tentativa de coleta.
