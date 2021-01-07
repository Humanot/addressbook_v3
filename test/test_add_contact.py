from model.contact import Contact

def test_create_new_contact(app):
    app.contact.create(
        Contact(firstname="Kirs", lastname="Vasiliev", homephone="555-666-666", mobile="89325848383", workphone="123",
                homephone2="444-444-555"))
