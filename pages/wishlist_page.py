from selene import browser, have



class WishPage:

    def open(self):
        browser.open('')

    def click_wish_list_header_logo(self):
        browser.element('.ut2-top-wishlist-count a.cm-tooltip.ty-wishlist__a > i.ut2-icon-baseline-favorite-border').click()

    def check_move_to_wishlist_page(self):
        browser.element('.ty-mainbox-container.clearfix').should(have.text('Отложенные товары'))