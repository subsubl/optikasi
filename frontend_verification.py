from playwright.sync_api import sync_playwright

def run():
    with sync_playwright() as p:
        browser = p.chromium.launch()
        page = browser.new_page()

        # Navigate to the quiz page
        page.goto("http://localhost:3000/stil-kviz")

        # Wait for network idle to ensure hydration
        page.wait_for_load_state('networkidle')

        # Wait for the step indicator to be visible
        page.wait_for_selector("nav[aria-label='Napredek kviza']")

        # Verify structure
        nav = page.locator("nav[aria-label='Napredek kviza']")
        ol = nav.locator("ol")

        # Check if OL exists
        if ol.count() == 0:
            print("Error: OL not found inside NAV")
            exit(1)

        # Check list items
        lis = ol.locator("li")
        count = lis.count()
        print(f"Found {count} list items")
        if count != 3:
            print(f"Error: Expected 3 steps, found {count}")
            exit(1)

        # Check aria-current on first step
        first_step = lis.nth(0)
        aria_current = first_step.get_attribute("aria-current")
        print(f"First step aria-current: {aria_current}")

        if aria_current != "step":
             print("Error: First step should have aria-current='step'")

        # Check sr-only text
        sr_text = first_step.locator(".sr-only").first.inner_text()
        print(f"SR Text: {sr_text}")

        # Take screenshot
        page.screenshot(path="verification_quiz.png")
        print("Screenshot saved to verification_quiz.png")

        browser.close()

if __name__ == "__main__":
    run()
