# Controle de releases

## Estratégia

`main` contém somente estado publicável e reproduzível. Desenvolvimento usa `feature/<id>-descricao`, correções `fix/<id>-descricao`, documentação `docs/<descricao>`.

Commits seguem Conventional Commits: `feat:`, `fix:`, `data:`, `docs:`, `test:`, `refactor:`, `chore:`, `perf:`. Mudança incompatível usa `!` ou `BREAKING CHANGE:`.

## Gates obrigatórios

1. `pytest -q`.
2. `python scripts/check_governance.py`.
3. `python scripts/validate_outputs.py`.
4. Snapshot contém fonte, versão e timestamps.
5. Manifesto de release contém SHA-256 dos artefatos centrais.
6. Nenhum P0 aplicável permanece aberto.
7. Mudança metodológica atualiza changelog, dicionário e documentação.

## Checklist de software

- [ ] Backlog/Issue vinculado.
- [ ] VERSION, pyproject e __version__ sincronizados.
- [ ] Changelog atualizado.
- [ ] Testes e gates verdes.
- [ ] ADR atualizado se necessário.
- [ ] Schema revisado se houver incompatibilidade.
- [ ] Artefatos regenerados.
- [ ] Tag `vX.Y.Z` somente após merge validado.

## Rollback

Código retorna à última tag/commit verde. Snapshot histórico nunca é corrigido silenciosamente. Release inválido gera incidente, restauração do último snapshot válido e novo release corrigido com justificativa.
