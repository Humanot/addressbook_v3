from mysql.connector import connect
from model.group import Group

class DbFixture:
    def __init__(self, host, name, user, password):
        self.host = host
        self.name = name
        self.user = user
        self.password = password
        self.connection = connect(host=host, database=name, user=user, password=password)
        self.connection.autocommit = True

    def get_list(self):
        #pass
        groups_list = []
        cursor = self.connection.cursor()
        try:
            cursor.execute("select group_id, group_name, group_header, group_footer from group_list")
            for row in cursor:
                (id, name, header, footer) = row
                groups_list.append(Group(id=str(id), name=name, header=header, footer=footer))
        finally:
            cursor.close()
        return groups_list

    def destroy(self):
        self.connection.close()