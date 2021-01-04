from model.group import Group

def test_create_new_group(app):
    old_groups = app.group.get_list()
    group = Group(name="Friends", header="Mine", footer="Dear ones")
    app.group.create(group)
    new_groups = app.group.get_list()
    assert len(old_groups) + 1 == len(new_groups)
    old_groups.append(group) #insert
    assert sorted(old_groups, key=Group.id_or_max) == sorted(new_groups, key=Group.id_or_max)

