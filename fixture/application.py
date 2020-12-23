from selenium.webdriver import Firefox
from fixture.session import SessionHelper

class Application:
    def __init__(self):
        self.driver = Firefox()
        self.driver.implicitly_wait(5)
        self.session = SessionHelper(self)

    def open_home_page(self):
        driver = self.driver
        driver.get("http://localhost/addressbook/")

    def open_groups_page(self):
        driver = self.driver
        driver.find_element_by_css_selector("#nav a[href='group.php']").click()

    def create_group(self, group):
        driver = self.driver
        self.open_groups_page()
        driver.find_element_by_name("new").click()

        # name
        group_name = driver.find_element_by_name("group_name")
        group_name.click()
        group_name.clear()
        group_name.send_keys(group.name)

        # header
        group_header = driver.find_element_by_name("group_header")
        group_header.click()
        group_header.clear()
        group_header.send_keys(group.header)

        # footer
        group_footer = driver.find_element_by_name("group_footer")
        group_footer.click()
        group_footer.clear()
        group_footer.send_keys(group.footer)
        driver.find_element_by_css_selector("#content [name=submit]").click()

        self.return_to_groups_page()

    def return_to_groups_page(self):
        driver = self.driver
        driver.find_element_by_css_selector(".msgbox [href='group.php']").click()

    def destroy(self):
        driver = self.driver
        driver.quit()