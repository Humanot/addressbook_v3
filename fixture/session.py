class SessionHelper:
    def __init__(self, app):
        self.app = app

    def login(self, username, password):
        driver = self.app.driver
        self.app.open_home_page()
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

    def logout(self):
        driver = self.app.driver
        driver.find_element_by_css_selector("#top [onclick='document.logout.submit();']").click()