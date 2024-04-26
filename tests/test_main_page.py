from pages.main_page import MainPage
import allure
from allure_commons.types import Severity
@allure.tag('web')
@allure.title('Successfully opened main page')
@allure.severity(Severity.CRITICAL)
@allure.label("owner", "checamaro")
@allure.feature("Main Page")
@allure.link("'https://planetainstrument.ru/'", name="Testing")
def test_main_page_elements():
    main_page = MainPage()
    with allure.step('Open main page'):
        main_page.open()
    with allure.step('Check for catalog exists'):
        main_page.check_for_catalog()
    with allure.step('Check for personal account button exists'):
        main_page.check_for_personal_account_button()
