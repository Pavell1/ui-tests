import random
from playwright.sync_api import Page
from utils.constants import LIST_OF_PRODUCTS
from page_objects import selectors


class GetProduct:
    @staticmethod
    def get_random_product_selector(category_selector: str, page: Page):
        # Открываем категорию
        page.click(category_selector)
        page.wait_for_selector(LIST_OF_PRODUCTS, state='visible')

        # Получаем список всех товаров в категории
        products = page.query_selector_all(selectors.items_in_category)

        # Выбираем случайный товар
        random_product = random.choice(products)
        product_name = random_product.inner_text()
        return random_product, product_name
