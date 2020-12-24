from model.group import Group

def test_create_new_group(app):
    app.group.create(Group(name="Friends", header="Mine", footer="Dear ones"))

