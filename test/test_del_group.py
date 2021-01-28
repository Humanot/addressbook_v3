from model.group import Group
from random import randrange, choice

def test_delete_first_group(app):
    if app.group.count() == 0:
        app.group.create(Group(name="Friends", header="Mine", footer="Dear ones"))
    old_groups = app.group.get_list()
    app.group.delete_first()
    assert len(old_groups) - 1 == app.group.count()
    new_groups = app.group.get_list()
    old_groups[0:1] = [] #pop/del
    assert old_groups == new_groups

def test_delete_some_group(app, db, check_ui):
    if len(db.get_list()) == 0:
        app.group.create(Group(name="Friends", header="Mine", footer="Dear ones"))
    old_groups = db.get_list()
    group = choice(old_groups)
    #index = randrange(len(old_groups))
    #app.group.delete_by_index(index)
    app.group.delete_by_id(group.id)
    new_groups = db.get_list()
    #old_groups[index:index+1] = [] #pop/del
    old_groups.remove(group)

    assert old_groups == new_groups
    if check_ui:
        assert sorted(new_groups, key=Group.id_or_max) == sorted(app.group.get_list(), key=Group.id_or_max)

