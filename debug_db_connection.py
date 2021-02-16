from fixture.orm import ORMFixture

db = ORMFixture(host="localhost", name="addressbook", user="root", password="")

try:
    l = db.get_contacts_list()
    for group in l:
        print(group)
    print(len(l))

finally:
    pass