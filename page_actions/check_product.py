from utils.selectors import * # лучше так не импортировать, лучше конкретные функции и тд


class CheckProduct:
    @staticmethod
    def check_product_in_cart(page, product_name):
        # Открываем корзину
        page.click(cart_icon)
        page.wait_for_load_state("networkidle")

        # Проверяем, что товар находится в корзине
        # такой таймаут плохо, что если все загрузиться через 1 секунду? а что если не успеет за 5?
        page.wait_for_timeout(5000)
        cart_items = page.query_selector_all(items_in_cart)
        assert any(
            item.inner_text() == product_name for item in cart_items), f"Product {product_name} not found in cart"