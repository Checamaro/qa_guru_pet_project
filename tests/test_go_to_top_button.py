from pages.main_page import main_page
import allure
from allure_commons.types import Severity


@allure.tag('web')
@allure.title('Successfully work of top button')
@allure.severity(Severity.CRITICAL)
@allure.label("owner", "checamaro")
@allure.feature("Main Page")
@allure.link("'https://planetainstrument.ru/'", name="Testing")
def test_return_to_the_top_button():
    main_page.open()

    main_page.scroll_down()
    main_page.click_top_button()

    main_page.check_for_go_up()
