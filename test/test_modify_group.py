from model.group import Group

def test_modify_first_group_name(app):
    if app.group.count() == 0:
        app.group.create(Group(name="Friends", header="Mine", footer="Dear ones"))
    group = Group(name="Relations")
    old_groups = app.group.get_list()
    group.id = old_groups[0].id #save id of changing group
    app.group.modify_first(group)
    new_groups = app.group.get_list()
    assert len(old_groups) == len(new_groups)
    old_groups[0] = group #name + id
    assert sorted(old_groups, key=Group.id_or_max) == sorted(new_groups, key=Group.id_or_max)

