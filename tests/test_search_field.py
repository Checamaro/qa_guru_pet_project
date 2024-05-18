from pages.main_page import main_page
import allure
from allure_commons.types import Severity


@allure.tag('web')
@allure.title('Successfully working of search field')
@allure.severity(Severity.CRITICAL)
@allure.label("owner", "checamaro")
@allure.feature("Main Page")
@allure.link("'https://planetainstrument.ru/'", name="Testing")
def test_main_page_elements():
    main_page.open()

    main_page.using_search_field()

    main_page.check_search_results()