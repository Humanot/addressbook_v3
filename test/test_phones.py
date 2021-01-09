from re import sub

def test_phones_on_home_page(app):
    contact_from_home_page = app.contact.get_list()[0]
    contact_from_edit_page = app.contact.get_info_from_edit_page(0)
    assert contact_from_home_page.homephone == clear(contact_from_edit_page.homephone)
    assert contact_from_home_page.workphone == clear(contact_from_edit_page.workphone)
    assert contact_from_home_page.mobile == clear(contact_from_edit_page.mobile)
    assert contact_from_home_page.homephone2 == clear(contact_from_edit_page.homephone2)

def test_phones_on_contact_view_page(app):
    contact_from_view_page = app.contact.get_info_from_view_page(0)
    contact_from_edit_page = app.contact.get_info_from_edit_page(0)
    assert contact_from_view_page.homephone == contact_from_edit_page.homephone
    assert contact_from_view_page.workphone == contact_from_edit_page.workphone
    assert contact_from_view_page.mobile == contact_from_edit_page.mobile
    assert contact_from_view_page.homephone2 == contact_from_edit_page.homephone2


def clear(s):
    return sub("[() -]", "", s)
