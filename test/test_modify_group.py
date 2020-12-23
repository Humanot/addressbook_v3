from model.group import Group

def test_modify_first_group_name(app):
    app.session.login(username="admin", password="secret")
    app.group.modify_first(Group(name="Relations"))
    app.session.logout()
