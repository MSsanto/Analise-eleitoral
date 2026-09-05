# Qualidade dos dados

## Controles automáticos

O pipeline verifica:
- existência dos manifests esperados;
- total lido por cargo versus total declarado no manifest;
- duplicidade de `id_tse` dentro do catálogo carregado;
- cobertura de UF para Deputado Federal;
- somatório das fontes de receita em relação ao total agregado;
- presença de valores negativos inesperados em agregados financeiros;
- timestamps das fontes e do snapshot;
- existência dos artefatos mínimos antes de um commit automático.

## Alertas que não devem virar conclusões editoriais

**Despesa paga igual a zero**: tratar como estado da carga, não como prova de que campanhas não efetuaram pagamentos.

**Histórico DDD sem correspondências**: indica que a camada histórica não vinculou candidaturas no snapshot; não permite inferir falta de atuação regional.

**Histórico do Senado pendente**: análises de mandato senatorial não devem ser apresentadas como completas.

**Ausência de patrimônio/finança**: significa que o pipeline não localizou registro compatível na carga consultada. Não deve ser transformada em “zero” sem respaldo do schema-fonte.

## Dimensões controladas

1. **Completude** — arquivos/manifests e cobertura esperada.
2. **Consistência** — totais, somatórios, denominadores e invariantes.
3. **Unicidade** — chaves e duplicidades.
4. **Freshness** — diferença entre geração da fonte e execução analítica.
5. **Linhagem** — commit, versão, schema e hashes.
6. **Reprodutibilidade** — mesma entrada + mesma versão deve produzir métricas semanticamente equivalentes.

Os SLAs iniciais estão em `config/governance.json`: candidaturas 12 h, finanças 18 h e Câmara 36 h.

## Severidade de falhas de dados

- `P0`: integridade/rastreabilidade comprometida; release bloqueado.
- `P1`: cobertura/freshness insuficiente para produto principal; release normalmente bloqueado.
- `P2`: degradação parcial com saída ainda interpretável.
- `P3`: problema sem impacto material nas métricas.
