from page_actions.get_product import GetProduct
from utils.selectors import *
from playwright.sync_api import Page


class AddProduct:
    get_product = GetProduct() # нигде не используется

    @staticmethod
    def add_product_to_cart(page: Page, product) -> None:  # добавить тип для продукта
        # Кликаем по товару
        product.click()
        #networkidle вижу второй раз - в константы
        page.wait_for_load_state("networkidle")

        # Добавляем товар в корзину
        page.click(success_button)

        # захардкоженных таймаутов не должно быть
        page.wait_for_timeout(5000)
        page.on("dialog", lambda dialog: dialog.accept())  # Принимаем диалоговое окно
