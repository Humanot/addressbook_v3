import allure
from pytest_bdd import given, when, then
from model.group import Group
from random import choice
import pytest


@given('a group list', target_fixture="group_list")
@allure.step('Given a group list')
def group_list(db):
    return db.get_list()


@given('a new group with <name>, <header> and <footer>', target_fixture="new_group")
@allure.step('Given a group list a new group with name={name}, header={header} and footer={footer}')
def new_group(name, header, footer):
    return Group(name=name, header=header, footer=footer)

@when('I add the group to the list')
def add_new_group(app, new_group):
    with allure.step('When I add the group to the list'):
        app.group.create(new_group)

@then('the new group list is equal to the old list with the added group')
def verify_group_added(db, group_list, new_group):
    with allure.step('Then the new group list is equal to the old list with the added group'):
        old_groups = group_list
        new_groups = db.get_list()
        old_groups.append(new_group)
        assert sorted(old_groups, key=Group.id_or_max) == sorted(new_groups, key=Group.id_or_max)


@given('a non-empty group list', target_fixture="non_empty_group_list")
@allure.step('Given a non-empty group list')
def non_empty_group_list(db, app):
    if len(db.get_list()) == 0:
        app.group.create(Group(name="Hiya"))
    return db.get_list()

@given('a random group from the list', target_fixture="random_group")
@allure.step('Given a random group from the list')
def random_group(non_empty_group_list):
    return choice(non_empty_group_list)

@when('I delete the group from the list')
def add_new_group(app, random_group):
    with allure.step(f'I delete the group {random_group} from the list'):
        app.group.delete_by_id(random_group.id)

@then('the new group list is equal to the old list without the deleted group')
def verify_group_added(db, non_empty_group_list, random_group, app, check_ui):
    with allure.step('Then the new group list is equal to the old list without the deleted group'):
        old_groups = non_empty_group_list
        new_groups = db.get_list()
        old_groups.remove(random_group)
        assert old_groups == new_groups

    if check_ui:
        with allure.step('Also check UI'):
            assert sorted(new_groups, key=Group.id_or_max) == sorted(app.group.get_list(), key=Group.id_or_max)
