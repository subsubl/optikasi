import { test, expect } from '@playwright/test';

test('Ray-Ban brand page loads correctly', async ({ page }) => {
  await page.goto('/znamke/ray-ban');
  
  // Check that the page title contains Ray-Ban
  const title = await page.title();
  expect(title).toContain('Ray-Ban');
  
  // Check that the main heading contains Ray-Ban
  const h1 = page.locator('h1');
  await expect(h1).toBeVisible();
  await expect(h1).toContainText('Ray-Ban');
});