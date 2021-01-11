from model.group import Group
from random import choice, randrange
from string import ascii_letters, digits, punctuation
from os.path import abspath, dirname, join
from json import dumps
import getopt, sys

n = 2
f = "groups.json" #data/groups.json

try:
    opts, args = getopt.getopt(sys.argv[1:], "n:f:", ["number of groups", "file"]) #prompts &getopt parser
except getopt.GetoptError as err:
    # print help information and exit:
    print(err)  # will print something like "option -a not recognized"
    getopt.usage()
    sys.exit(2)

for o, a in opts:
    if o == "-n":
        n = int(a)
    elif o == "-f":
        f = a

def random_string(prefix, maxlen):
    symbols = ascii_letters + digits + punctuation + " " * 10
    return prefix + "".join([choice(symbols) for i in range(randrange(maxlen))])


test_data = [Group(name="Friends", header="Mine", footer="Dear ones"),
             Group(name="", header="", footer="")] + [
                Group(name=random_string("name", 10), header=random_string("header", 20),
                      footer=random_string("footer", 20)) for i in range(n)]

test_data_file = join(dirname(abspath(__file__)), "../data/", f)

with open(test_data_file, mode="w") as file:
    file.write(dumps(test_data, default=lambda x: x.__dict__, indent=2))
# test_data = [
#     Group(name=name, header=header, footer=footer)
#     for name in ["", random_string("name", 10)]
#     for header in ["", random_string("header", 20)]
#     for footer in ["", random_string("footer", 20)]
# ]

