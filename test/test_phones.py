from re import sub

def test_phones_on_home_page(app):
    contact_from_home_page = app.contact.get_list()[0]
    contact_from_edit_page = app.contact.get_info_from_edit_page(0)
    assert contact_from_home_page.all_phones_from_homepage == merge_phones_like_on_home_page(contact_from_edit_page)

def test_phones_on_contact_view_page(app):
    contact_from_view_page = app.contact.get_info_from_view_page(0)
    contact_from_edit_page = app.contact.get_info_from_edit_page(0)
    assert contact_from_view_page.homephone == contact_from_edit_page.homephone
    assert contact_from_view_page.workphone == contact_from_edit_page.workphone
    assert contact_from_view_page.mobile == contact_from_edit_page.mobile
    assert contact_from_view_page.homephone2 == contact_from_edit_page.homephone2


def clear(s):
    return sub("[() -]", "", s)

def merge_phones_like_on_home_page(contact):
    phones_list = [contact.homephone, contact.workphone, contact.mobile, contact.homephone2]
    return "\n".join(filter(lambda x: x != "",
                            map(lambda x: clear(x),
                                filter(lambda x: x is not None, phones_list))))