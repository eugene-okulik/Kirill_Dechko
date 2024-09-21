import re

from playwright.sync_api import Page, expect, Route


def test_change_data_on_page(page: Page):
    def handle_route(route: Route):
        route.fetch()
    new_text = 'яблокофон 15 про'
    page.route(re.compile(r'.*-pro-.*'), handle_route)
    page.goto("https://www.apple.com/shop/buy-iphone", timeout=90000, wait_until="domcontentloaded")
    page.click("//*[contains(@class, 'rf-hcard-content-swatchescontainer') and contains(@aria-label, 'Pro')]")
    page.wait_for_selector("h2.rf-digitalmat-overlay-header", timeout=30000)
    page.evaluate(f"document.querySelector('h2.rf-digitalmat-overlay-header').textContent = '{new_text}'")
    new_text_path = page.locator("//h2[@data-autom='DigitalMat-overlay-header-0-0']")
    expect(new_text_path).to_contain_text(new_text)
