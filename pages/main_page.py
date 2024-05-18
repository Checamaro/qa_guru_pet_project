from selene import browser, have, command
import allure
from selenium.webdriver import Keys


class MainPage:

    def open(self):
        with allure.step('Open main page'):
            browser.open('')

    def scroll_down(self):
        with allure.step('Scroll down'):
            browser.element('.bottom-copyright').perform(command.js.scroll_into_view)
    def click_top_button(self):
        with allure.step('Click top button'):
            browser.element('.ab__scroll_to_top_button').click()


    def using_search_field(self):
        with allure.step('Using search field'):
            browser.element('.ty-search-block__input').type('Бензопила').send_keys(Keys.ENTER)

    def check_search_results(self):
        with allure.step('Checking results of using search field'):
            browser.element('.ty-mainbox-title__left').should(have.text('Результаты поиска'))


    def check_for_catalog(self):
        with allure.step('Check for catalog exists'):
            browser.element(
                '.top-menu-grid-vetrtical').should(
                have.text('Каталог товаров'))

    def check_for_personal_account_button(self):
        with allure.step('Check for personal account button exists'):
            browser.element('.ut2-top-my-account').should(
                have.text('Аккаунт'))

    def check_for_go_up(self):
        with allure.step('Check for go up button works'):
            browser.element('.ty-geo-maps__geolocation__opener-text').should(have.text('Москва'))


main_page = MainPage()
