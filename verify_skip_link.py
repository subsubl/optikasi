from playwright.sync_api import sync_playwright

def run(playwright):
    browser = playwright.chromium.launch()
    page = browser.new_page()

    # Navigate to the home page
    page.goto("http://localhost:3000")

    # Wait for hydration/load
    page.wait_for_load_state("networkidle")

    # Press Tab to focus the first element (which should be our skip link)
    page.keyboard.press("Tab")

    # Wait for the transition to complete (300ms duration)
    page.wait_for_timeout(500)

    # Get the focused element
    focused_element = page.evaluate("document.activeElement")

    # Check if the focused element is our skip link
    is_skip_link = page.evaluate("document.activeElement.textContent.includes('Preskoči na vsebino')")

    if is_skip_link:
        print("Success: Skip link is focused!")
    else:
        print("Failure: Skip link is NOT focused.")
        print(f"Focused element text: {page.evaluate('document.activeElement.textContent')}")

    # Take a screenshot
    page.screenshot(path="skip_link_verification.png")

    browser.close()

with sync_playwright() as playwright:
    run(playwright)
