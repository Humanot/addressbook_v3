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

    def is_logged_in(self):
        return len(self.app.driver.find_elements_by_css_selector("#top [onclick='document.logout.submit();']")) > 0

    def is_logged_in_as(self, username):
        return self.get_logged_user() == username

    def get_logged_user(self):
        driver = self.app.driver
        return driver.find_element_by_css_selector("form[name=logout] b").text[1:-1]

    def ensure_login(self, username, password):
        if self.is_logged_in():
            if self.is_logged_in_as(username):
                return
            else:
                self.logout()
        self.login(username, password)

    def logout(self):
        driver = self.app.driver
        driver.find_element_by_css_selector("#top [onclick='document.logout.submit();']").click()

    def ensure_logout(self):
        if self.is_logged_in():
            self.logout()