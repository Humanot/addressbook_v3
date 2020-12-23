from selenium.webdriver import Firefox

class Application:
    def __init__(self):
        self.driver = Firefox()
        self.driver.implicitly_wait(5)

    def open_home_page(self):
        driver = self.driver
        driver.get("http://localhost/addressbook/")

    def login(self, username, password):
        driver = self.driver
        self.open_home_page()
        # username
        username_field = driver.find_element_by_name("user")
        username_field.clear()
        username_field.send_keys(username)

        # password
        pass_field = driver.find_element_by_name("pass")
        pass_field.click()
        pass_field.clear()
        pass_field.send_keys(password)
        driver.find_element_by_css_selector("input[value=Login]").click()

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

    def logout(self):
        driver = self.driver
        driver.find_element_by_css_selector("#top [onclick='document.logout.submit();']").click()

    def destroy(self):
        driver = self.driver
        driver.quit()