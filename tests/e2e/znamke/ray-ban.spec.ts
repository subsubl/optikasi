import { test, expect } from '@playwright/test';

test('Ray-Ban brand page loads correctly', async ({ page }) => {
  await page.goto('/znamke/ray-ban');

  // The h1 shows the brand tagline; brand name appears in the page/SEO title
  await expect(page.locator('h1').first()).toBeVisible();
  await expect(page).toHaveTitle(/Ray-Ban/);
});
