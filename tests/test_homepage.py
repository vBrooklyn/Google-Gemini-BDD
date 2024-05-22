import os

import google.generativeai as genai
import pytest
from dotenv import load_dotenv

from pom.checkout_page import CheckoutPage
from pom.homepage_nav import HomepageNav
from pom.product_page import ProductPage

# Load environment variables from .env
load_dotenv()

api_key = os.getenv("API_KEY")

genai.configure(api_key=api_key)

# Gemini Prompt
PROMPT = """You are a user testing a website. Follow these steps:
                1. Click on the first link using 'homepage_nav.click_on_nav_link'
                2. Select the second product using 'homepage_nav.click_on_product'
                3. On the product page, click 'product_page.click_add_to_cart_button'
                4. Click 'product_page.click_get_checkout_button'
                5. On the checkout page, click 'checkout_page.click_get_pay_now_button' """


@pytest.mark.usefixtures('setup')
class TestHomepage:

    @pytest.fixture(autouse=True)
    def initialize_page_objects(self, setup):
        """Initialize page objects using the driver from 'setup' fixture."""
        self.homepage_nav = HomepageNav(self.driver)
        self.product_page = ProductPage(self.driver)
        self.checkout_page = CheckoutPage(self.driver)
        self.model_name = 'gemini-1.5-pro-latest'  # Set the model name as a class attribute
        self.PROMPT = PROMPT

    def test_checkout_error_message(self):
        """Test the checkout error message."""
        # Gemini Tools
        tools = [
            self.homepage_nav.click_on_nav_link,
            self.homepage_nav.click_on_product,
            self.product_page.click_add_to_cart_button,
            self.product_page.click_get_checkout_button,
            self.checkout_page.click_get_pay_now_button
        ]

        # Create the model within the test
        model = genai.GenerativeModel(
            model_name=self.model_name,
            tools=tools,
            system_instruction=self.PROMPT
        )
        chat = model.start_chat(enable_automatic_function_calling=True)
        chat.send_message("Start testing the website.")

        # Assertion
        assert self.checkout_page.get_email_error_text().text == 'Enter an email'
