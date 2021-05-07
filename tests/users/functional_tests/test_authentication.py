"""
Functional test using Selenium to test the behavior
Check README file to to launch this test.
"""

from django.contrib.staticfiles.testing import StaticLiveServerTestCase
from selenium import webdriver

from purbeurre.settings import BASE_DIR


firefox_options = webdriver.FirefoxOptions()
firefox_options.headless = True


class SeleniumRegisterTest(StaticLiveServerTestCase):
    @classmethod
    def setUpClass(cls):
        super().setUpClass()
        geckodriver = str(BASE_DIR / "webdrivers" / "geckodriver")
        cls.driver = webdriver.Firefox(
            executable_path=geckodriver, options=firefox_options
        )
        cls.driver.implicitly_wait(10)
        cls.driver.maximize_window()

    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()
        super().tearDownClass()

    def test_register(self):
        """Launches the functional test for the registration
        and automatical login feature"""
        # Access register page and fill fields
        self.driver.get("%s%s" % (self.live_server_url, "/register/"))
        email_input = self.driver.find_element_by_name("email")
        email_input.send_keys("usertest1@email.com")
        username_input = self.driver.find_element_by_name("username")
        username_input.send_keys("usertest1")
        password_input = self.driver.find_element_by_name("password1")
        password_input.send_keys("Password+1234")
        confirm_password_input = self.driver.find_element_by_name("password2")
        confirm_password_input.send_keys("Password+1234")
        # Click on button which registers + login automatically
        self.driver.find_element_by_class_name("btn").click()
        # Checks if icon "mon_compte" in DOM, means logged in
        self.driver.find_element_by_id("mon_compte")
