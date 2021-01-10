from model.group import Group
import pytest

test_data = [Group(name="Friends", header="Mine", footer="Dear ones"),
             Group(name="", header="", footer="")]

@pytest.mark.parametrize("group", test_data, ids=[repr(x) for x in test_data])
def test_create_new_group(app, group):
    old_groups = app.group.get_list()
    app.group.create(group)
    assert len(old_groups) + 1 == app.group.count()
    new_groups = app.group.get_list()
    old_groups.append(group) #insert
    assert sorted(old_groups, key=Group.id_or_max) == sorted(new_groups, key=Group.id_or_max)

