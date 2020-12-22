from selenium.webdriver import Firefox
driver = Firefox()
driver.implicitly_wait(5)


def open_home_page():
    driver.get("http://localhost/addressbook/")

def login():
    #username
    username_field = driver.find_element_by_name("user")
    username_field.clear()
    username_field.send_keys("admin")

    #password
    pass_field = driver.find_element_by_name("pass")
    pass_field.click()
    pass_field.clear()
    pass_field.send_keys("secret")
    driver.find_element_by_css_selector("input[value=Login]").click()

def open_groups_page():
    driver.find_element_by_css_selector("#nav a[href='group.php']").click()

def create_group():
    driver.find_element_by_name("new").click()

    #name
    group_name = driver.find_element_by_name("group_name")
    group_name.click()
    group_name.clear()
    group_name.send_keys("Friends")

    #header
    group_header = driver.find_element_by_name("group_header")
    group_header.click()
    group_header.clear()

    #footer
    group_header.send_keys("Mine")
    group_footer = driver.find_element_by_name("group_footer")
    group_footer.click()
    group_footer.clear()
    group_footer.send_keys("Dear ones")
    driver.find_element_by_css_selector("#content [name=submit]").click()

def return_to_groups_page():
    driver.find_element_by_css_selector(".msgbox [href='group.php']").click()

def logout():
    driver.find_element_by_css_selector("#top [onclick='document.logout.submit();']").click()


open_home_page()
login()
open_groups_page()
create_group()
return_to_groups_page()
logout()

driver.quit()
