from model.group import Group
from random import randrange

def test_modify_first_group_name(app):
    if app.group.count() == 0:
        app.group.create(Group(name="Friends", header="Mine", footer="Dear ones"))
    group = Group(name="Relations")
    old_groups = app.group.get_list()
    group.id = old_groups[0].id #save id of changing group
    app.group.modify_first(group)
    assert len(old_groups) == app.group.count()
    new_groups = app.group.get_list()
    old_groups[0] = group #name + id
    assert sorted(old_groups, key=Group.id_or_max) == sorted(new_groups, key=Group.id_or_max)

def test_modify_some_group_name(app):
    if app.group.count() == 0:
        app.group.create(Group(name="Friends", header="Mine", footer="Dear ones"))
    group = Group(name="Relations")
    old_groups = app.group.get_list()
    index = randrange(len(old_groups))
    group.id = old_groups[index].id #save id of changing group
    app.group.modify_by_index(index, group)
    assert len(old_groups) == app.group.count()
    new_groups = app.group.get_list()
    old_groups[index] = group #name + id
    assert sorted(old_groups, key=Group.id_or_max) == sorted(new_groups, key=Group.id_or_max)
