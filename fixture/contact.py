from selenium.webdriver.support.ui import Select

class ContactHelper:
    def __init__(self, app):
        self.app = app

    def create(self, contact_data):
        driver = self.app.driver
        driver.find_element_by_css_selector("#nav a[href='edit.php']").click()
        self.fill_contact_info(contact_data)
        driver.find_element_by_css_selector("form[name=theform] input[name=submit]").click()
        self.return_to_home_page()

    def return_to_home_page(self):
        driver = self.app.driver
        driver.find_element_by_css_selector(".msgbox a[href='index.php']").click()

    def is_filled(self, value):
        if value is not None:
            return True

    def change_field_value(self, data_field, field_name):
        if self.is_filled(data_field):
            driver = self.app.driver
            name_field = driver.find_element_by_name(field_name)
            name_field.click()
            name_field.clear()
            name_field.send_keys(data_field)

    def upload_photo(self, data_field, field_name):
        if self.is_filled(data_field):
            driver = self.app.driver
            photo_field = driver.find_element_by_name(field_name)
            photo_field.send_keys(data_field)

    def change_listbox_value(self, box_name, value):
        if self.is_filled(value):
            driver = self.app.driver
            select_list = Select(driver.find_element_by_name(box_name))
            select_list.select_by_visible_text(value)

    def fill_contact_info(self, contact_data):
        self.change_field_value(contact_data.firstname, "firstname")
        self.change_field_value(contact_data.middlename, "middlename")
        self.change_field_value(contact_data.lastname, "lastname")
        self.change_field_value(contact_data.nickname, "nickname")

        self.upload_photo(contact_data.photo, "photo")

        self.change_field_value(contact_data.title, "title")
        self.change_field_value(contact_data.company, "company")
        self.change_field_value(contact_data.address, "address")

        self.change_field_value(contact_data.homephone, "home")
        self.change_field_value(contact_data.mobile, "mobile")
        self.change_field_value(contact_data.workphone, "work")
        self.change_field_value(contact_data.fax, "fax")

        #Emails:
        self.change_field_value(contact_data.email, "email")
        self.change_field_value(contact_data.email2, "email2")
        self.change_field_value(contact_data.email3, "email3")

        self.change_field_value(contact_data.homepage, "homepage")

        #Birthday
        self.change_listbox_value("bday", contact_data.bday)
        self.change_listbox_value("bmonth", contact_data.bmonth)
        self.change_field_value(contact_data.byear, "byear")

        #Anniversary
        self.change_listbox_value("aday", contact_data.aday)
        self.change_listbox_value("amonth", contact_data.amonth)
        self.change_field_value(contact_data.ayear, "ayear")

        #contact_group
        self.change_listbox_value("new_group", contact_data.group)

        self.change_field_value(contact_data.address2, "address2")
        self.change_field_value(contact_data.homephone2, "phone2")
        self.change_field_value(contact_data.notes, "notes")





