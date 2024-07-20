from utils.constants import URL
from page_actions.get_product import GetProduct
from utils.selectors import *
from playwright.sync_api import Page


class AddProduct:
    get_product = GetProduct()

    @staticmethod
    def add_product_to_cart(page: Page, product):
        # Кликаем по товару
        product.click()
        page.wait_for_load_state("networkidle")

        # Добавляем товар в корзину
        page.click(success_button)
        page.wait_for_timeout(5000)
        page.on("dialog", lambda dialog: dialog.accept())  # Принимаем диалоговое окно

        # Возвращаемся на главную страницу
        page.goto(URL)
        page.wait_for_load_state("networkidle")