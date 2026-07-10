import { test, expect } from '@playwright/test';

test('homepage loads with correct title', async ({ page }) => {
  await page.goto('/');

  // The homepage uses a custom title that differs from the default template
  await expect(page).toHaveTitle(/Optika\.si \| Očala, Kontaktne leče in Pregled vida/);
});

test('storitve page loads', async ({ page }) => {
  await page.goto('/storitve');

  // Check if it loads without crashing
  await expect(page.locator('h1').first()).toBeVisible();
});
