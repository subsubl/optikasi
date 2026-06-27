import { test, expect } from '@playwright/test';

test('homepage loads with correct title', async ({ page }) => {
  await page.goto('/');

  // Title template is '%s | Optika Ljubljana'
  await expect(page).toHaveTitle('Optika.si | Očala, Kontaktne leče in Pregled vida (Ljubljana & Slovenija)');
});

test('storitve page loads', async ({ page }) => {
  await page.goto('/storitve');

  // Check if it loads without crashing
  await expect(page.locator('h1').first()).toBeVisible();
});
