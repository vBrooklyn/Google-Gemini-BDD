from selenium.webdriver.remote.webelement import WebElement

from base.seleniumbase import SeleniumBase


class CheckoutPage(SeleniumBase):
    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver
        self.__pay_now_button = '#checkout-pay-button'
        self.__email_error_text = '#error-for-email'

    def get_pay_now_button(self) -> WebElement:
        '''Get pay now button
        :return: WebElement'''
        return self.is_visible('css', self.__pay_now_button, 'Pay now button')

    def get_email_error_text(self) -> WebElement:
        '''Get email error text
        :return: WebElement'''
        return self.is_visible('css', self.__email_error_text, 'Email error text')

    def click_get_pay_now_button(self) -> None:
        '''Click pay now button'''

        self.get_pay_now_button().click()