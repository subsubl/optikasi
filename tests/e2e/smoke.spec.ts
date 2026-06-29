import { test, expect } from '@playwright/test';

test('homepage loads with correct title', async ({ page }) => {
  await page.goto('/');

  // Title template is '%s' for index, falling back to app.vue defaults
  await expect(page).toHaveTitle(/Optika\.si/);
});

test('storitve page loads', async ({ page }) => {
  await page.goto('/storitve');

  // Check if it loads without crashing
  await expect(page.locator('h1').first()).toBeVisible();
});
