# import pytest
import allure
from model.group import Group
# from data.groups import constant as test_data

# @pytest.mark.parametrize("group", groups, ids=[repr(x) for x in test_data])
# def test_create_new_group(app, data_groups):
def test_create_new_group(app, db, json_groups):
    group = json_groups
    with allure.step('Given a group list'):
        #old_groups = app.group.get_list()
        old_groups = db.get_list()
    with allure.step(f'When I add the group {group} to the list'):
        app.group.create(group)
    with allure.step('Then the new group list is equal to the old list with the added group'):
        #assert len(old_groups) + 1 == app.group.count() #old hashing through ui len
        #new_groups = app.group.get_list()
        new_groups = db.get_list()
        old_groups.append(group)  # insert
        assert sorted(old_groups, key=Group.id_or_max) == sorted(new_groups, key=Group.id_or_max)
