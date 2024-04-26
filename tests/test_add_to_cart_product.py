from pages.catalog_page import CatalogPage
from pages.cart_page import CartPage
import allure
from allure_commons.types import Severity


@allure.tag('web')
@allure.title('Successfully added to cart product')
@allure.severity(Severity.CRITICAL)
@allure.label("owner", "checamaro")
@allure.feature("Cart check")
@allure.link("'https://planetainstrument.ru/'", name="Testing")
def test_add_to_cart_product():
    catalog_page = CatalogPage()
    cart_page = CartPage()
    with allure.step('Open main page'):
        catalog_page.open()
    with allure.step('Open catalog'):
        catalog_page.catalog_button_click()
    with allure.step('Choose electric instrument'):
        catalog_page.catalog_electric_instrument_click()
    with allure.step('Choose wrench'):
        catalog_page.catalog_electric_instrument_wrench_click()
    with allure.step('Click sorting button'):
        catalog_page.click_sort_button()
    with allure.step('Click sorting by increasing price'):
        catalog_page.click_sort_by_price_from_cheap_button()
    with allure.step('Choose Makita wrench'):
        catalog_page.catalog_electric_instrument_wrench_makita_add_to_cart()
    with allure.step('Close cart announcement'):
        catalog_page.close_cart_announcement()
    with allure.step('Click cart'):
        cart_page.cart_button_click()
    with allure.step('Assertion that cart has a right product'):
        catalog_wrench_name = catalog_page.get_catalog_wrench_makita_name()
        cart_wrench_name = cart_page.get_cart_wrench_name()
        assert catalog_wrench_name == cart_wrench_name
