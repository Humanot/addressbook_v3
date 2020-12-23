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

    def delete_first(self):
        driver = self.app.driver
        self.open_groups_page()
        driver.find_element_by_name("selected[]").click()
        driver.find_element_by_name("delete").click()
        self.return_to_groups_page()

    def return_to_groups_page(self):
        driver = self.app.driver
        driver.find_element_by_css_selector(".msgbox [href='group.php']").click()