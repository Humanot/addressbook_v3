from selenium.webdriver.support.ui import Select

class ContactHelper:
    def __init__(self, app):
        self.app = app

    def create(self, contact_data):
        driver = self.app.driver
        driver.find_element_by_css_selector("#nav a[href='edit.php']").click()
        self.fill_contact_info(contact_data)
        self.return_to_home_page()

    def return_to_home_page(self):
        driver = self.app.driver
        driver.find_element_by_css_selector(".msgbox a[href='index.php']").click()

    def change_field_value(self, data_field, field_name):
        driver = self.app.driver
        name_field = driver.find_element_by_name(field_name)
        name_field.click()
        name_field.clear()
        name_field.send_keys(data_field)

    def fill_contact_info(self, contact_data):
        driver = self.app.driver
        self.change_field_value(contact_data.firstname, "firstname")
        self.change_field_value("Dunno", "middlename")
        self.change_field_value(contact_data.lastname, "lastname")
        self.change_field_value("Viking", "nickname")

        #photo
        photo_field = driver.find_element_by_name("photo")
        photo_field.send_keys("D:/1. Pictures/Avatars/team av/231587506.jpg")

        self.change_field_value("Title", "title")
        self.change_field_value("Coins", "company")
        self.change_field_value("Karbisheva 12 - 44", "address")

        self.change_field_value(contact_data.homephone, "home")
        self.change_field_value(contact_data.mobile, "mobile")
        self.change_field_value(contact_data.workphone, "work")
        self.change_field_value("no", "fax")

        #Emails:
        self.change_field_value("blizzard@gmail.com", "email")
        self.change_field_value("Ugu", "email2")
        self.change_field_value("main@gnu.tu", "email3")

        self.change_field_value("vk.com", "homepage")

        #Birthday
        bday_select = Select(driver.find_element_by_name("bday"))
        bday_select.select_by_visible_text("10")
        bmonth_select = Select(driver.find_element_by_name("bmonth"))
        bmonth_select.select_by_visible_text("May")
        self.change_field_value("1989", "byear")

        #Anniversary
        aday_select = Select(driver.find_element_by_name("aday"))
        aday_select.select_by_visible_text("14")
        amonth_select = Select(driver.find_element_by_name("amonth"))
        amonth_select.select_by_visible_text("March")
        self.change_field_value("2000", "ayear")

        group_select = Select(driver.find_element_by_name("new_group"))
        group_select.select_by_visible_text("[none]")

        self.change_field_value("Theres nothing", "address2")
        self.change_field_value(contact_data.homephone2, "phone2")
        self.change_field_value("Origato", "notes")

        driver.find_element_by_css_selector("form[name=theform] input[name=submit]").click()

