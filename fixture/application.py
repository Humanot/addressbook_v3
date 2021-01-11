from selenium.webdriver import Chrome, Firefox, Ie
from fixture.session import SessionHelper
from fixture.group import GroupHelper
from fixture.contact import ContactHelper

class Application:
    def __init__(self, browser, base_url):
        self.base_url = base_url

        if browser == "chrome":
            self.driver = Chrome()
        elif browser == "firefox":
            self.driver = Firefox()
        elif browser == "ie":
            self.driver = Ie()
        else:
            raise ValueError(f"Unrecognized browser {browser}!")

        self.driver.implicitly_wait(1)
        self.session = SessionHelper(self)
        self.group = GroupHelper(self)
        self.contact = ContactHelper(self)

    def open_home_page(self):
        driver = self.driver
        driver.get(self.base_url)

    def is_valid(self):
        try:
            self.driver.current_url
            return True
        except:
            return False

    def destroy(self):
        driver = self.driver
        driver.quit()