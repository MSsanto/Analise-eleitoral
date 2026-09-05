# Dashboard Next.js — engenharia de frontend

Esta trilha adiciona uma nova camada web ao projeto analítico sem substituir, nesta fase, o dashboard HTML existente.

## Objetivo de portfólio

Demonstrar uma aplicação Next.js moderna com foco explícito em qualidade de entrega:

- Next.js 16.3.x e TypeScript;
- App Router;
- componentes testáveis;
- testes unitários/componente com Vitest + Testing Library;
- testes E2E com Playwright;
- API Route para health check;
- GitHub Actions;
- Pull Request template e revisão de código;
- integração incremental com os snapshots analíticos já produzidos pelo repositório.

## Estratégia

O novo frontend vive em `web/`. O dashboard atual em `dashboard/` continua disponível como baseline até que a nova camada cubra os fluxos essenciais e passe pelos gates de qualidade.

## Gates antes do merge

1. testes unitários passam;
2. build de produção passa;
3. E2E crítico passa;
4. PR descreve impacto e evidências de teste;
5. mudanças metodológicas de dados continuam obedecendo às regras existentes do projeto.
