import { test, expect } from '@playwright/test';

test('homepage loads with correct title', async ({ page }) => {
  await page.goto('/');

  // Title template is '%s | Optika.si'
  await expect(page).toHaveTitle(/Optika.si/);
});

test('storitve page loads', async ({ page }) => {
  await page.goto('/storitve');

  // Check if it loads without crashing
  await expect(page.locator('h1').first()).toBeVisible();
});

test('o-nas page loads with correct heading', async ({ page }) => {
  await page.goto('/o-nas');

  await expect(page.locator('h1').first()).toContainText('O Nas');
});
