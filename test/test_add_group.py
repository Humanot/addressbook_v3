# import pytest
from model.group import Group
# from data.groups import constant as test_data

# @pytest.mark.parametrize("group", groups, ids=[repr(x) for x in test_data])
def test_create_new_group(app, data_groups):
    group = data_groups
    old_groups = app.group.get_list()
    app.group.create(group)
    assert len(old_groups) + 1 == app.group.count()
    new_groups = app.group.get_list()
    old_groups.append(group)  # insert
    assert sorted(old_groups, key=Group.id_or_max) == sorted(new_groups, key=Group.id_or_max)
