from selene import browser, have
import allure


class WishPage:

    def open(self):
        with allure.step('Open main page'):
            browser.open('')

    def click_wish_list_header_logo(self):
        with allure.step('Check for catalog exists'):
            browser.element(
                '.ut2-top-wishlist-count').click()

    def check_move_to_wishlist_page(self):
        with allure.step('Check for personal account button exists'):
            browser.element('.ty-mainbox-container.clearfix').should(have.text('Отложенные товары'))


wishlist_page = WishPage()
