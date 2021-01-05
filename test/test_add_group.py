from model.group import Group

def test_create_new_group(app):
    old_groups = app.group.get_list()
    group = Group(name="Friends", header="Mine", footer="Dear ones")
    app.group.create(group)
    assert len(old_groups) + 1 == app.group.count()
    new_groups = app.group.get_list()
    old_groups.append(group) #insert
    assert sorted(old_groups, key=Group.id_or_max) == sorted(new_groups, key=Group.id_or_max)

