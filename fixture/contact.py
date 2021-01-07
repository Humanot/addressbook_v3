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

    def fill_contact_info(self, contact_data):
        driver = self.app.driver
        firstname_field = driver.find_element_by_name("firstname")
        firstname_field.click()
        firstname_field.clear()
        firstname_field.send_keys(contact_data.firstname)

        middlename_field = driver.find_element_by_name("middlename")
        middlename_field.click()
        middlename_field.clear()
        middlename_field.send_keys("Dunno")

        lastname_field = driver.find_element_by_name("lastname")
        lastname_field.click()
        lastname_field.clear()
        lastname_field.send_keys(contact_data.lastname)

        nickname_field = driver.find_element_by_name("nickname")
        nickname_field.click()
        nickname_field.clear()
        nickname_field.send_keys("Viking")

        #photo
        photo_field = driver.find_element_by_name("photo")
        photo_field.send_keys("D:/1. Pictures/Avatars/team av/231587506.jpg")

        title_field = driver.find_element_by_name("title")
        title_field.click()
        title_field.clear()
        title_field.send_keys("Title")
        company_field = driver.find_element_by_name("company")
        company_field.click()
        company_field.clear()
        company_field.send_keys("Coins")
        address_field = driver.find_element_by_name("address")
        address_field.click()
        address_field.clear()
        address_field.send_keys("Karbisheva 12 - 44")

        #homephone
        homephone_field = driver.find_element_by_name("home")
        homephone_field.click()
        homephone_field.clear()
        homephone_field.send_keys(contact_data.homephone)

        mobile_field = driver.find_element_by_name("mobile")
        mobile_field.click()
        mobile_field.clear()
        mobile_field.send_keys(contact_data.mobile)

        workphone_field = driver.find_element_by_name("work")
        workphone_field.click()
        workphone_field.clear()
        workphone_field.send_keys(contact_data.workphone)

        fax_field = driver.find_element_by_name("fax")
        fax_field.click()
        fax_field.clear()
        fax_field.send_keys("no")
        email_field = driver.find_element_by_name("email")
        email_field.click()
        email_field.clear()
        email_field.send_keys("blizzard@gmail.com")
        email2_field = driver.find_element_by_name("email2")
        email2_field.click()
        email2_field.clear()
        email2_field.send_keys("Ugu")
        email3_field = driver.find_element_by_name("email3")
        email3_field.click()
        email3_field.clear()
        email3_field.send_keys("main@gnu.tu")
        homepage_field = driver.find_element_by_name("homepage")
        homepage_field.click()
        homepage_field.clear()
        homepage_field.send_keys("vk.com")
        bday_select = Select(driver.find_element_by_name("bday"))
        bday_select.select_by_visible_text("10")
        bmonth_select = Select(driver.find_element_by_name("bmonth"))
        bmonth_select.select_by_visible_text("May")
        byear_field = driver.find_element_by_name("byear")
        byear_field.click()
        byear_field.clear()
        byear_field.send_keys("1989")
        aday_select = Select(driver.find_element_by_name("aday"))
        aday_select.select_by_visible_text("14")
        amonth_select = Select(driver.find_element_by_name("amonth"))
        amonth_select.select_by_visible_text("March")
        ayear_field = driver.find_element_by_name("ayear")
        ayear_field.click()
        ayear_field.clear()
        ayear_field.send_keys("2000")
        group_select = Select(driver.find_element_by_name("new_group"))
        group_select.select_by_visible_text("[none]")
        address2_field = driver.find_element_by_name("address2")
        address2_field.click()
        address2_field.clear()
        address2_field.send_keys("Theres nothing")

        homephone2_field = driver.find_element_by_name("phone2")
        homephone2_field.click()
        homephone2_field.clear()
        homephone2_field.send_keys(contact_data.homephone2)

        notes_field = driver.find_element_by_name("notes")
        notes_field.click()
        notes_field.clear()
        notes_field.send_keys("Origato")
        driver.find_element_by_css_selector("form[name=theform] input[name=submit]").click()