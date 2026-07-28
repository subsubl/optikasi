import subprocess
import time
import urllib.request
from playwright.sync_api import sync_playwright

def wait_for_server(url, timeout=30):
    start = time.time()
    while time.time() - start < timeout:
        try:
            r = urllib.request.urlopen(url)
            if r.getcode() == 200:
                print("Server is up!")
                return True
        except Exception:
            pass
        time.sleep(1)
    return False

# Start server
server = subprocess.Popen(['node', '.output/server/index.mjs'], stdout=subprocess.PIPE, stderr=subprocess.PIPE)

if wait_for_server('http://localhost:3000'):
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        context = browser.new_context(record_video_dir="/home/jules/verification/videos")
        page = context.new_page()
        page.goto('http://localhost:3000/kontakt')

        # Scroll down to make form visible
        page.evaluate('window.scrollBy(0, 500)')
        time.sleep(1) # wait for any lazy load / transitions

        screenshot_path = "/home/jules/verification/screenshots/booking-form.png"
        page.screenshot(path=screenshot_path, full_page=True)

        context.close()
        browser.close()

        print(f"Screenshot saved to {screenshot_path}")

# Cleanup
server.terminate()
