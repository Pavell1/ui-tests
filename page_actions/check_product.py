from page_objects import selectors
from utils import constants
from playwright.sync_api import Page


class CheckProduct:
    @staticmethod
    def check_product_in_cart(page: Page, product_name):
        # Открываем корзину
        page.click(selectors.cart_icon)
        page.wait_for_load_state(constants.NETWORKIDLE)

        # Проверяем, что товар находится в корзине
        page.wait_for_load_state()
        page.wait_for_selector(constants.LIST_OF_PRODUCTS, state='visible')
        cart_items = page.query_selector_all(selectors.items_in_cart)
        assert (
            any(item.inner_text() == product_name for item in cart_items)), f"Product {product_name} not found in cart"
