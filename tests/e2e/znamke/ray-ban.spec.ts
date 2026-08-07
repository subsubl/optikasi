import { test, expect } from '@playwright/test'

test('Ray-Ban brand page has correct heading', async ({ page }) => {
  await page.goto('/znamke/ray-ban')
  
  // Check that the main heading is visible and contains 'Ray-Ban'
  const heading = page.getByRole('heading', { name: 'Ray-Ban' })
  await expect(heading).toBeVisible()
  await expect(heading).toContainText('Ray-Ban')
})