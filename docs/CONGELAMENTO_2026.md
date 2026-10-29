# Congelamento do ciclo eleitoral 2026

**Estado:** congelado  
**Data efetiva:** 26/10/2026  
**Retomada prevista:** ciclo eleitoral de 2028, somente mediante autorização explícita.

## Regra operacional

O encerramento de 2026 deixou o projeto como arquivo histórico. Não devem ocorrer coleta, regeneração de análises, publicação de derivados ou releases automáticas. A chegada de 2028, por si só, não reabre o projeto.

Qualquer retomada exige, antes de executar código ou reativar automações:
1. autorização explícita do responsável;
2. registro documentado do escopo e da data da retomada;
3. revisão das fontes, critérios de atualidade e controles de qualidade;
4. validação e aprovação das alterações necessárias.

## Incidente identificado em 29/10/2026

O workflow `.github/workflows/analise-eleitoral.yml` do repositório `MSsanto/Analise-eleitoral` permaneceu agendado mesmo depois do congelamento do repositório-fonte `MSsanto/Elei-oes-2026`.

- Execução: [run #195](https://github.com/MSsanto/Analise-eleitoral/actions/runs/40951104751), ID `40951104751`.
- Evento: `schedule`, em 29/10/2026 às 20:40 UTC.
- Resultado: falha no *freshness gate*; o snapshot rejeitado foi colocado em quarentena.
- Validação: ignorada porque a geração foi reprovada.
- Publicação: os derivados não foram publicados. O workflow gravou somente o diagnóstico de falha em `data/status/analysis-run.json`, no commit [`8544189`](https://github.com/MSsanto/Analise-eleitoral/commit/85441895ff95ab3be72cb0afe33a0c5a84a76790).

## Contenção

Os workflows de geração analítica e de release foram tornados inertes:
- removidos os gatilhos de agenda, execução manual e push normal na branch `main`;
- mantido apenas um branch guard explícito e improvável (`__freeze_guard__`);
- adicionada uma condição de bloqueio no job (`if: ${{ false }}`);
- reduzida a permissão de conteúdo para leitura.

O workflow de qualidade permanece disponível para verificar mudanças propostas; ele não coleta dados nem publica análises. Nenhuma análise foi reexecutada como parte desta contenção e nenhum derivado foi atualizado.

## Estado dos dados

O snapshot validado anterior permanece como referência histórica. Uma tentativa reprovada não substitui nem invalida retroativamente o último snapshot validado, e atraso ou ausência de atualização não deve ser interpretado como irregularidade.
