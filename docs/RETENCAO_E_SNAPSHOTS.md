# Retenção e snapshots

`snapshot-latest.json` aponta para o último snapshot validado e só é substituído após todos os gates. `data/derived/history/YYYY-MM-DD.json` é histórico diário e imutável por padrão. Manifestos de release são preservados como trilha de auditoria.

Política inicial: snapshots diários por pelo menos 120 dias; snapshots mensais por 36 meses ou até o encerramento do projeto, o que for maior; manifestos de release com retenção indefinida; derivados regeneráveis podem ser reconstruídos quando snapshot e versão de código estiverem preservados.

Séries temporais só comparam snapshots semanticamente compatíveis, mesmo `analysis_schema_version` ou migração explícita, e mudanças metodológicas documentadas.
