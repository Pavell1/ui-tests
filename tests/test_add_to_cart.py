import pytest

from page_actions.get_product import GetProduct
from utils.constants import SELECTORS


@pytest.mark.parametrize("product_type, selector", SELECTORS)
def test_add_random_product_to_cart(page, product_type, selector, add_product, check_product):
    random_product, product_name = GetProduct.get_random_product_selector(selector, page)
    add_product.add_product_to_cart(page, random_product)
    check_product.check_product_in_cart(page, product_name)
