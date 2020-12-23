from model.group import Group

def test_create_new_group(app):
    app.session.login(username="admin", password="secret")
    app.group.create(Group(name="Friends", header="Mine", footer="Dear ones"))
    app.session.logout()

