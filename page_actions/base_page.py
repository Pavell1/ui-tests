import playwright
from playwright.sync_api import expect


class BasePage:
    def __init__(self, page: playwright.sync_api.Page):
        self.page = page

    def click(self, selector, wait_until_visible=True, timeout=3000):
        if wait_until_visible:
            self.wait_until_element_is_visible(selector, timeout=timeout)
        self.page.locator(selector).first.click()

    def wait_until_element_is_visible(self, selector, timeout=5000):
        if (
                self.page.locator(selector).first.wait_for(state="visible", timeout=timeout)
                is None
        ):
            return self.page.locator(selector).first
