from model.group import Group

def test_create_new_group(app):
    old_groups = app.group.get_list()
    app.group.create(Group(name="Friends", header="Mine", footer="Dear ones"))
    new_groups = app.group.get_list()
    assert len(old_groups) + 1 == len(new_groups)

