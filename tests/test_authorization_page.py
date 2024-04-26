from pages.authorization_page import AuthorizationPage
import allure
from allure_commons.types import Severity
from data.users import User


@allure.tag('web')
@allure.title('Successfully authorized user')
@allure.severity(Severity.CRITICAL)
@allure.label("owner", "checamaro")
@allure.feature("Authorization page")
@allure.link("'https://planetainstrument.ru/'", name="Testing")
def test_successful_authorization():
    Polygraf = User(
        user_email='788test567@gmail.com',
        user_password='qwerty123456',
        user_first_name='Полиграф',
        user_last_name='Шариков'
    )


    authorization_page = AuthorizationPage()
    with allure.step('Open main page'):
        authorization_page.open()
    with allure.step('Click account button'):
        authorization_page.account_button()
    with allure.step('Click authorization button'):
        authorization_page.authorization_button()
    with allure.step('Fill in user email and password'):
        authorization_page.fill_in_valid_user_data(Polygraf)
    with allure.step('Click submit button'):
        authorization_page.submit()
    with allure.step('Click logged account button'):
        authorization_page.logged_account_button()
    with allure.step('Checking for successful authorization'):
        authorization_page.check_for_successful_authorization(Polygraf)
