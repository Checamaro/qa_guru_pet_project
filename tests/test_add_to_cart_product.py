from pages.catalog_page import catalog_page
from pages.cart_page import cart_page
import allure
from allure_commons.types import Severity


@allure.tag('web')
@allure.title('Successfully added to cart product')
@allure.severity(Severity.CRITICAL)
@allure.label("owner", "checamaro")
@allure.feature("Cart Page")
@allure.link("'https://planetainstrument.ru/'", name="Testing")
def test_add_to_cart_product():
    catalog_page.open()

    catalog_page.catalog_button_click()
    catalog_page.catalog_electric_instrument_click()
    catalog_page.catalog_electric_instrument_wrench_click()
    catalog_page.click_sort_button()
    catalog_page.click_sort_by_price_from_cheap_button()
    catalog_page.catalog_electric_instrument_wrench_makita_add_to_cart()
    catalog_page.close_cart_announcement()
    cart_page.cart_button_click()

    catalog_wrench_name = catalog_page.get_catalog_wrench_makita_name()
    cart_wrench_name = cart_page.get_cart_wrench_name()
    assert catalog_wrench_name == cart_wrench_name
