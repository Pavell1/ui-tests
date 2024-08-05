from playwright.sync_api import Page

from page_actions.base_page import BasePage
from page_actions.get_product import GetProduct
from utils.selectors import *


class AddProduct:
    get_product = GetProduct()  # нигде не используется

    @staticmethod
    def add_product_to_cart(page: Page, product) -> None:  # добавить тип для продукта
        product.click()

        # тут просто добавил для примера, на самом деле нужно наследоваться от base page
        base_page = BasePage(page=page)
        base_page.click(selector=success_button)

        # page.wait_for_load_state("networkidle")
        #
        # # Добавляем товар в корзину
        # page.click(success_button)
        #
        # # захардкоженных таймаутов не должно быть
        # page.wait_for_timeout(5000)
        page.on("dialog", lambda dialog: dialog.accept())  # Принимаем диалоговое окно
