import { test, expect } from '@playwright/test';

test('homepage loads with correct title', async ({ page }) => {
  await page.goto('/');

  // Title template is '%s | Optika.si'
  await expect(page).toHaveTitle(/Optika.si/);
  await expect(page.locator('text=Kaj Pravijo Naše Stranke')).toBeVisible();
  await expect(page.locator('form #name')).toBeVisible();
  await expect(page.locator('form #email')).toBeVisible();
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

test('blog page loads with articles', async ({ page }) => {
  await page.goto('/blog');

  await expect(page.locator('h1').first()).toContainText('Blog');
  await expect(page).toHaveTitle(/Blog/);
  const articles = page.locator('article, .bg-white.rounded-lg');
  await expect(articles.first()).toBeVisible();
});

test('blog article page loads with full title and content', async ({ page }) => {
  await page.goto('/blog/progresivna-stekla');

  await expect(page.locator('h1').first()).toContainText('Progresivna stekla');
  await expect(page).toHaveTitle(/Progresivna stekla.*Optika Ljubljana/);
});

test('kontakt page loads with form and contact info', async ({ page }) => {
  await page.goto('/kontakt');

  await expect(page.locator('h1').first()).toContainText('Stopite v Stik');
  await expect(page.locator('input#name')).toBeVisible();
  await expect(page.locator('input#email')).toBeVisible();
  await expect(page.locator('#main-content a[href="tel:+38641788516"]')).toBeVisible();
  await expect(page.locator('#main-content a[href="mailto:info@optikasi.si"]')).toBeVisible();
});

test('cenik page loads with pricing tables', async ({ page }) => {
  await page.goto('/cenik');

  await expect(page.locator('h1').first()).toContainText('Cenik Storitev');
  await expect(page.locator('text=Pogosta Vprašanja o Ceniku')).toBeVisible();
  await expect(page.locator('a[href*="/kontakt?service=pregled-vida"]').first()).toBeVisible();
});

test('booking form populates service and message from query parameters', async ({ page }) => {
  await page.goto('/kontakt?service=pregled-vida&sporocilo=Pozdravljeni+test');

  const serviceSelect = page.locator('select#service');
  await expect(serviceSelect).toBeVisible();
  await expect(serviceSelect).toHaveValue('pregled-vida');

  const messageTextarea = page.locator('textarea#message');
  await expect(messageTextarea).toHaveValue('Pozdravljeni test');
});

test('stil kviz interactive flow and reset', async ({ page }) => {
  await page.goto('/stil-kviz');

  await expect(page.locator('[data-hydrated="true"]')).toBeVisible();
  await expect(page.locator('h1')).toContainText('Stil Kviz');

  // Step 1: Face Shape (e.g. Ovalna)
  await page.locator('button:has-text("Ovalna")').click();

  // Step 2: Style (e.g. Sodobno)
  await expect(page.locator('button:has-text("Sodobno")')).toBeVisible();
  await page.locator('button:has-text("Sodobno")').click();

  // Step 3: Budget (e.g. Premium)
  await expect(page.locator('button:has-text("Premium")')).toBeVisible();
  await page.locator('button:has-text("Premium")').click();

  // Step 4: Results
  await expect(page.locator('text=Vaše priporočilo')).toBeVisible();
  await expect(page.locator('text=Minimalistični rimless okvirji')).toBeVisible();

  // Reset quiz
  await page.locator('button:has-text("Ponovno Reši Kviz")').click();
  await expect(page.locator('text=Kakšna je oblika vašega obraza?')).toBeVisible();
});
