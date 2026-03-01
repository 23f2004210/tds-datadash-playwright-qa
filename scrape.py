from playwright.sync_api import sync_playwright
import re

seeds = list(range(9, 19))
total_sum = 0

with sync_playwright() as p:
    browser = p.chromium.launch(headless=True)
    page = browser.new_page()

    for seed in seeds:
        url = f"https://sanand0.github.io/tdsdata/js_table/?seed={seed}"
        page.goto(url)
        page.wait_for_timeout(2000)

        tables = page.locator("table")
        count = tables.count()

        for i in range(count):
            table_text = tables.nth(i).inner_text()
            numbers = re.findall(r"-?\d+", table_text)
            total_sum += sum(map(int, numbers))

    browser.close()

print("FINAL TOTAL:", total_sum)
