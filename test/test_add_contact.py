from model.contact import Contact

def test_create_new_contact(app):
    old_contacts = app.contact.get_list()
    contact = Contact(firstname="Kirs", lastname="Vasiliev", homephone="555-666-666", mobile="8-(932)-584-83-83",
                      workphone="[123]",
                      homephone2="444444555")
    app.contact.create(contact)
    assert len(old_contacts) + 1 == app.contact.count()
    new_contacts = app.contact.get_list()
    old_contacts.append(contact)
    assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max)
