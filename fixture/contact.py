from selenium.webdriver.support.ui import Select
from model.contact import Contact

class ContactHelper:

    contacts_list_cache = None

    def __init__(self, app):
        self.app = app

    def create(self, contact_data):
        driver = self.app.driver
        driver.find_element_by_css_selector("#nav a[href='edit.php']").click()
        self.fill_contact_info(contact_data)
        driver.find_element_by_css_selector("form[name=theform] input[name=submit]").click()
        self.return_to_home_page()

        self.contacts_list_cache = None

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

    def get_list(self):
        if self.contacts_list_cache is None:
            driver = self.app.driver
            self.contacts_list_cache = []
            self.app.open_home_page()
            contacts_rows = driver.find_elements_by_css_selector("#maintable tr[name=entry]")
            for row in contacts_rows:
                #cells = row.find_elements_by_tag_name("td)"
                id = row.find_element_by_css_selector("td input").get_attribute("value")
                firstname = row.find_elements_by_tag_name("td")[2].text
                lastname = row.find_elements_by_tag_name("td")[1].text

                self.contacts_list_cache.append(Contact(id=id, firstname=firstname, lastname=lastname))
        return list(self.contacts_list_cache)

    def count(self):
        driver = self.app.driver
        return len(driver.find_elements_by_css_selector("#maintable tr[name=entry]"))

    def open_view_page_by_index(self, index):
        driver = self.app.driver
        self.app.open_home_page()
        contact_row = driver.find_elements_by_css_selector("#maintable tr[name=entry]")[index]
        cell = contact_row.find_elements_by_tag_name("td")[6]
        cell.contact_row.find_elements_by_tag_name("a").click()

    def open_edit_page_by_index(self, index):
        driver = self.app.driver
        self.app.open_home_page()
        contact_row = driver.find_elements_by_css_selector("#maintable tr[name=entry]")[index]
        cell = contact_row.find_elements_by_tag_name("td")[7]
        cell.contact_row.find_elements_by_tag_name("a").click()