# Gestão de incidentes

Severidade: SEV-1 dado publicado incorreto/perda de rastreabilidade; SEV-2 pipeline fora do SLA ou divergência relevante; SEV-3 falha parcial sem perda de integridade; SEV-4 cosmético/documental.

Cada incidente registra ID `INC-YYYY-NNN`, data/hora UTC, severidade, status, componente, `data_release_id`, impacto, detecção, causa raiz, mitigação, correção definitiva, prevenção e backlog relacionado.

Incidente que afeta número publicado exige correção versionada, nunca edição silenciosa. SEV-1 e SEV-2 geram ação preventiva no backlog. A causa raiz distingue fonte, transporte, transformação, regra analítica e apresentação.
