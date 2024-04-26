from selene import browser, have
from data.users import User



class CatalogPage:

    def open(self):
        browser.open('')

    def catalog_button_click(self):
        browser.element('.ty-dropdown-box.top-menu-grid-vetrtical div.ty-dropdown-box__title.cm-combination').click()

    def catalog_electric_instrument_click(self):
        browser.element('.first-lvl:nth-child(3) a.ty-menu__item-link.a-first-lvl span.menu-lvl-ctn span:nth-child(2) > span.v-center').click()
    def catalog_electric_instrument_wrench_click(self):
        browser.element('.level-0:nth-child(1) a:nth-child(1)').click()

    def get_catalog_wrench_makita_name(self):
        browser.element('.grid-list div:nth-child(1) div.ty-column4:nth-child(4)').should(have.text('Гайковерт ударный MAKITA TD0101F'))

    def click_sort_button(self):
        browser.element('.ty-sort-dropdown:nth-child(1) a.ty-sort-dropdown__wrapper').click()

    def click_sort_by_price_from_cheap_button(self):
        browser.element('.sort-by-price-asc.ty-sort-dropdown__content-item').click()

    def catalog_electric_instrument_wrench_makita_add_to_cart(self):
        browser.element('.icon_button div.cm-reload-45264:nth-child(1) button').click()

    def close_cart_announcement(self):
        browser.element('.notification-content-extended.cm-auto-hide:nth-child(43) h1:nth-child(1) > span.cm-notification-close.close').click()

