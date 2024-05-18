from pages.authorization_page import authorization_page
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

    authorization_page.open()

    authorization_page.account_button()
    authorization_page.authorization_button()
    authorization_page.fill_in_valid_user_data(Polygraf)
    authorization_page.submit()
    authorization_page.logged_account_button()

    authorization_page.check_for_successful_authorization(Polygraf)
