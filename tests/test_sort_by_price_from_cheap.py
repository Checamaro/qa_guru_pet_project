from pages.catalog_page import CatalogPage
from pages.main_page import MainPage
import allure
from allure_commons.types import Severity
@allure.tag('web')
@allure.title('Successfully sorting by price from cheap check')
@allure.severity(Severity.CRITICAL)
@allure.label("owner", "checamaro")
@allure.feature("Catalog Page")
@allure.link("'https://planetainstrument.ru/'", name="Testing")
def test_sort_by_price_from_cheap():
    catalog_page = CatalogPage()
    main_page = MainPage()
    with allure.step('Open main page'):
        main_page.open()
    with allure.step('Click catalog'):
        catalog_page.catalog_button_click()
    with allure.step('Click catalog battery instrument'):
        catalog_page.catalog_battery_instrument_click()
    with allure.step('Click sort products'):
        catalog_page.click_sort_button()
    with allure.step('Click sort products by price from cheap'):
        catalog_page.click_sort_by_price_from_cheap_button()
    with allure.step('Check correct sorting'):
        catalog_page.check_correct_sorting()
