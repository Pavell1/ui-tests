from page_objects.selectors import success_button
from playwright.sync_api import Page
from utils.constants import NETWORKIDLE


class AddProduct:

    @staticmethod
    def add_product_to_cart(page: Page, product) -> None:  # добавить тип для продукта / как понять какой тип у продукта?
        # Кликаем по товару
        product.click()
        page.wait_for_load_state(NETWORKIDLE)

        # Добавляем товар в корзину
        page.click(success_button)

        # Принимаем диалоговое окно
        page.on("dialog", lambda dialog: dialog.accept())


