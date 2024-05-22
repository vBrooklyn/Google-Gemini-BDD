from selenium.webdriver.remote.webelement import WebElement

from base.seleniumbase import SeleniumBase


class ProductPage(SeleniumBase):
    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver
        self.__add_to_cart_button = 'button[class*=button--large]'
        self.__checkout_button = '#update-cart'

    def get_add_to_cart_button(self) -> WebElement:
        return self.is_visible('css', self.__add_to_cart_button, 'Add to cart button')

    def get_checkout_button(self) -> WebElement:
        return self.is_visible('css', self.__checkout_button, 'Checkout button')

    def click_add_to_cart_button(self) -> None:
        self.get_add_to_cart_button().click()

    def click_get_checkout_button(self) -> None:
        self.get_checkout_button().click()