from pages.wishlist_page import wishlist_page
import allure
from allure_commons.types import Severity


@allure.tag('web')
@allure.title('Successfully opened wishlist page')
@allure.severity(Severity.CRITICAL)
@allure.label("owner", "checamaro")
@allure.feature("Wishlist Page")
@allure.link("'https://planetainstrument.ru/'", name="Testing")
def test_main_page_elements():
    wishlist_page.open()

    wishlist_page.click_wish_list_header_logo()

    wishlist_page.check_move_to_wishlist_page()
