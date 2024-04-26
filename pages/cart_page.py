from selene import browser, have
from data.users import User



class CartPage:

    def open(self):
        browser.open('')

    def cart_button_click(self):
        browser.element('.ut2-top-cart-content').click()


    def get_cart_wrench_name(self):
        browser.element('.ty-cart-items__list-item div.ty-cart-items__list-item-desc > a:nth-child(1)').should(have.text('Гайковерт ударный MAKITA TD0101F'))

