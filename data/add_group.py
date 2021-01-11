from model.group import Group
from random import choice, randrange
from string import ascii_letters, digits, punctuation


def random_string(prefix, maxlen):
    symbols = ascii_letters + digits + punctuation + " " * 10
    return prefix + "".join([choice(symbols) for i in range(randrange(maxlen))])


test_data = [Group(name="Friends", header="Mine", footer="Dear ones"),
             Group(name="", header="", footer="")] + [
                Group(name=random_string("name", 10), header=random_string("header", 20),
                      footer=random_string("footer", 20)) for i in range(5)]

constant = [Group(name="Friends", header="Mine", footer="Dear ones"),
             Group(name="", header="", footer="")]

# test_data = [
#     Group(name=name, header=header, footer=footer)
#     for name in ["", random_string("name", 10)]
#     for header in ["", random_string("header", 20)]
#     for footer in ["", random_string("footer", 20)]
# ]