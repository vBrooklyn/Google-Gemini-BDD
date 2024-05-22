from typing import List

from selenium.webdriver.remote.webelement import WebElement

from base.seleniumbase import SeleniumBase


class HomepageNav(SeleniumBase):

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver
        self.__nav_links = '.navigation__tier-1 li'
        self.__products = 'div[class*=product-block] img[class*=rimage__image]'

    def get_nav_links(self) -> List[WebElement]:
        '''Return WebElements for nav links'''
        return self.are_present('css', self.__nav_links, 'Header Navigation Links')

    def get_products(self) -> List[WebElement]:
        '''Return WebElements for products'''
        return self.are_present('css', self.__products, 'Products')

    def click_on_nav_link(self) -> None:
        '''Click on a nav link'''
        nav_links = self.get_nav_links()
        nav_links[0].click()

    def click_on_product(self) -> None:
        '''Click on a product'''
        products = self.get_products()
        products[1].click()
