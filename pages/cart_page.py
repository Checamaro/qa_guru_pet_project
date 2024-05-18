from selene import browser, have
import allure


class CartPage:

    def open(self):
        browser.open('')

    def cart_button_click(self):
        with allure.step('Click cart'):
            browser.element('.ut2-top-cart-content').click()

    def get_cart_wrench_name(self):
        with allure.step('Get wrench name in cart'):
            browser.element('.ty-cart-items__list-item').should(
                have.text('Гайковерт ударный MAKITA TD0101F'))


cart_page = CartPage()
