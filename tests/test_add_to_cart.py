
from page_actions.get_product import GetProduct as GetProduct
from page_actions.add_product import AddProduct as AddProduct
from page_actions.check_product import CheckProduct as CheckProduct
from utils.constants import SELECTORS

import pytest


@pytest.mark.parametrize("product_type, selector", SELECTORS)
def test_add_random_product_to_cart(page, product_type, selector):
    random_product, product_name = GetProduct.get_random_product_selector(selector, page)
    AddProduct.add_product_to_cart(page, random_product)
    # AddProduct and CheckProduct вынести в фикстуры
    CheckProduct.check_product_in_cart(page, product_name)



