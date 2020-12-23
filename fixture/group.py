class GroupHelper:
    def __init__(self, app):
        self.app = app

    def open_groups_page(self):
        driver = self.app.driver
        driver.find_element_by_css_selector("#nav a[href='group.php']").click()

    def create(self, group):
        driver = self.app.driver
        self.open_groups_page()
        driver.find_element_by_name("new").click()
        self.fill_group_fields(group)
        driver.find_element_by_css_selector("#content [name=submit]").click()
        self.return_to_groups_page()

    def fill_group_fields(self, group):
        driver = self.app.driver

        self.change_field_value("group_name", group.name)
        self.change_field_value("group_header", group.header)
        self.change_field_value("group_footer", group.header)

    def change_field_value(self, field_name, value):
        driver = self.app.driver
        if value is not None:
            group_name = driver.find_element_by_name(field_name)
            group_name.click()
            group_name.clear()
            group_name.send_keys(value)

    def delete_first(self):
        driver = self.app.driver
        self.open_groups_page()
        self.select_first_group()
        driver.find_element_by_name("delete").click()
        self.return_to_groups_page()

    def select_first_group(self):
        driver = self.app.driver
        driver.find_element_by_name("selected[]").click()

    def modify_first(self, new_group_data):
        driver = self.app.driver
        self.open_groups_page()
        self.select_first_group()
        driver.find_element_by_name("edit").click()
        self.fill_group_fields(new_group_data)
        driver.find_element_by_name("update").click()
        self.return_to_groups_page()

    def return_to_groups_page(self):
        driver = self.app.driver
        driver.find_element_by_css_selector(".msgbox [href='group.php']").click()