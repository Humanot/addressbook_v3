from model.group import Group
import pytest
from random import choice, randrange
from string import ascii_letters, digits, punctuation


def random_string(prefix, maxlen):
    symbols = ascii_letters + digits + punctuation + " " * 10
    return prefix + "".join([choice(symbols) for i in range(randrange(maxlen))])


test_data = [Group(name="Friends", header="Mine", footer="Dear ones"),
             Group(name="", header="", footer="")] + [
                Group(name=random_string("name", 10), header=random_string("header", 20),
                      footer=random_string("footer", 20)) for i in range(5)]

# test_data = [
#     Group(name=name, header=header, footer=footer)
#     for name in ["", random_string("name", 10)]
#     for header in ["", random_string("header", 20)]
#     for footer in ["", random_string("footer", 20)]
# ]

@pytest.mark.parametrize("group", test_data, ids=[repr(x) for x in test_data])
def test_create_new_group(app, group):
    old_groups = app.group.get_list()
    app.group.create(group)
    assert len(old_groups) + 1 == app.group.count()
    new_groups = app.group.get_list()
    old_groups.append(group)  # insert
    assert sorted(old_groups, key=Group.id_or_max) == sorted(new_groups, key=Group.id_or_max)
