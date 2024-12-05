import time
import unittest

from selenium import webdriver
from selenium.webdriver.common.by import By


class TestLoginPage(unittest.TestCase):
    def setUp(self):
        self.browser = webdriver.Chrome()
        self.browser.get("http://register.csinc.ie/")
        # Wait for the contents to load...
        self.browser.implicitly_wait(10)

    def tearDown(self):
        self.browser.close()

    def test_login_page(self):
        # We should be on the login page:
        self.assertIn("Log in to CSLinc", self.browser.title)

        # Email element
        email_element = self.browser.find_element(By.ID, "Email")
        email_element.send_keys("nobody@example.com")
        self.assertEqual("nobody@example.com", email_element.get_attribute("value"))


if __name__ == "__main__":
    unittest.main()
