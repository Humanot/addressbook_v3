from model.contact import Contact

def test_create_new_contact(app):
    old_contacts = app.contact.get_list()
    contact = Contact(firstname="Kirs", lastname="Vasiliev", homephone="555666666", mobile="89325848383",
                      workphone="123",
                      homephone2="444444555")
    app.contact.create(contact)
    assert len(old_contacts) + 1 == app.contact.count()
    new_contacts = app.contact.get_list()
    old_contacts.append(contact)
    assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max)
