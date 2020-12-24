from model.group import Group

def test_modify_first_group_name(app):
    if app.group.count() == 0:
        app.group.create(Group(name="Friends", header="Mine", footer="Dear ones"))
    app.group.modify_first(Group(name="Relations"))

