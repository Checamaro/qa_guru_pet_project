from selene import browser, have
import allure


class CatalogPage:

    def open(self):
        with allure.step('Open main page'):
            browser.open('')

    def catalog_button_click(self):
        with allure.step('Open catalog'):
            browser.element(
                '.top-menu-grid-vetrtical').click()

    def catalog_battery_instrument_click(self):
        browser.element('.first-lvl:nth-child(4)').click()

    def catalog_electric_instrument_click(self):
        with allure.step('Choose electric instrument'):
            browser.element(
                '.first-lvl:nth-child(3)').click()

    def catalog_electric_instrument_wrench_click(self):
        with allure.step('Choose wrench'):
            browser.element('.level-0:nth-child(1) a:nth-child(1)').click()

    def get_catalog_wrench_makita_name(self):
        with allure.step('Get wrench catalog name'):
            wrench_cat = browser.element('.cat-view-grid')
            wrench_cat.should(have.text('Гайковерт ударный MAKITA TD0101F'))

    def click_sort_button(self):
        browser.element('#sw_elm_sort_fields').click()

    def click_sort_by_price_from_cheap_button(self):
        with allure.step('Click sorting by increasing price'):
            browser.element('.sort-by-price-asc').click()

    def catalog_electric_instrument_wrench_makita_add_to_cart(self):
        with allure.step('Choose Makita wrench'):
            browser.element('.icon_button div.cm-reload-45264:nth-child(1) button').click()

    def close_cart_announcement(self):
        with allure.step('Close cart announcement'):
            browser.element(
                '.notification-content-extended.cm-auto-hide:nth-child(43) h1:nth-child(1) > span.cm-notification-close.close').click()


catalog_page = CatalogPage()
