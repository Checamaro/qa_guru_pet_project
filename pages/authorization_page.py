from selene import browser, have
from data.users import User
import allure


class AuthorizationPage:

    def open(self):
        with allure.step('Open main page'):
            browser.open('')

    def account_button(self):
        with allure.step('Click account button'):
            browser.element('.ut2-top-my-account').click()

    def authorization_button(self):
        with allure.step('Click authorization button'):
            browser.element('.cm-dialog-auto-size.ty-btn').click()

    def fill_in_valid_user_data(self, user):
        with allure.step('Fill in user email and password'):
            browser.element('#login_popup122').type(user.user_email)
            browser.element('#psw_popup122').type(user.user_password)

    def submit(self):
        with allure.step('Click submit button'):
            browser.element('.ty-btn__login').click()

    def logged_account_button(self):
        with allure.step('Click logged account button'):
            browser.element(
                '.ut2-top-my-account.ty-float-right').click()

    def check_for_successful_authorization(self, users: User):
        with allure.step('Checking for successful authorization'):
            browser.element('.ty-account-info__name').should(have.text(
                f'{users.user_first_name} {users.user_last_name}'
            ))


authorization_page = AuthorizationPage()
