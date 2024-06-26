import allure
from allure_commons.types import Severity
from pages.main_page import main_page


@allure.tag('web')
@allure.title('Successfully opened main page')
@allure.severity(Severity.CRITICAL)
@allure.label("owner", "checamaro")
@allure.feature("Main Page")
@allure.link("'https://planetainstrument.ru/'", name="Testing")
def test_main_page_elements():
    main_page.open()

    main_page.check_for_catalog()
    main_page.check_for_personal_account_button()
