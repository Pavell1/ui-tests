import pytest
from playwright.sync_api import sync_playwright
from utils.constants import URL


@pytest.fixture(scope="function")
def browser():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        yield browser
        browser.close()


@pytest.fixture(scope="function")
def page(browser):
    context = browser.new_context()
    page = context.new_page()
    page.goto(URL)
    page.wait_for_load_state("networkidle")
    yield page
    context.close()