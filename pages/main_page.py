from selene import browser, have


class MainPage:

    def open(self):
        browser.open('')

    def check_for_catalog(self):
        browser.element('.ty-dropdown-box.top-menu-grid-vetrtical div.ty-dropdown-box__title.cm-combination').should(
            have.text('Каталог товаров'))

    def check_for_personal_account_button(self):
        browser.element('.ut2-top-my-account.ty-float-right div.ty-dropdown-box__title').should(
            have.text('Аккаунт'))
