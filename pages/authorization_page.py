from selene import browser, have
from data.users import User, Username


class AuthorizationPage:

    def open(self):
        browser.open('')

    def account_button(self):
        browser.element('.ut2-top-my-account.ty-float-right div.ty-dropdown-box__title').click()

    def authorization_button(self):
        browser.element('.cm-dialog-auto-size.ty-btn.ty-btn__secondary').click()

    def fill_in_valid_user_data(self, user):
        browser.element('#login_popup122').type(user.user_email)
        browser.element('#psw_popup122').type(user.user_password)

    def submit(self):
        browser.element('.ty-btn__login.ty-btn__secondary.ty-btn span:nth-child(1)').click()

    def logged_account_button(self):
        browser.element('.row-fluid div.span16 div.row-fluid div.span5.account-cart-grid div.ut2-top-my-account.ty-float-right div.ty-dropdown-box div.ty-dropdown-box__title.cm-combination a:nth-child(1) > span:nth-child(2)').click()

    # def check_for_successful_authorization(self, users):
    #     browser.element('.ty-account-info__name').should(have.texts(
    #         f'{users.user_first_name} {users.user_last_name}'
    #     ))

    def check_for_successful_authorization(self, username):
        browser.element('.ty-account-info__name').should(have.texts(
            f'{username.user_first_name} {username.user_last_name}'
        ))