import { test, expect } from '@playwright/test';

test('homepage loads with correct title', async ({ page }) => {
  await page.goto('/');

  // Title template contains 'Ljubljana'
  await expect(page).toHaveTitle(/Ljubljana/);
});

test('storitve page loads', async ({ page }) => {
  await page.goto('/storitve');

  // Check if it loads without crashing
  await expect(page.locator('h1').first()).toBeVisible();
});
