import { expect, test } from '@playwright/test';

test('loads the dashboard and exposes the health endpoint', async ({ page, request }) => {
  await page.goto('/');

  await expect(
    page.getByRole('heading', { level: 1, name: 'Análise Eleitoral 2026' }),
  ).toBeVisible();
  await expect(page.getByText('Revisão por Pull Request')).toBeVisible();

  const health = await request.get('/api/health');
  expect(health.ok()).toBeTruthy();
  await expect(health.json()).resolves.toMatchObject({ status: 'ok' });
});
