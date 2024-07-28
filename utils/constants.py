URL = "https://www.demoblaze.com/"
PRODUCT_TYPES = ["Phones", "Laptops", "Monitors"]
SELECTORS = [(ptype, f"a.list-group-item:has-text('{ptype}')") for ptype in PRODUCT_TYPES]
NETWORKIDLE = "networkidle"
LIST_OF_PRODUCTS = "#tbodyid"