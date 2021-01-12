from mysql.connector import connect

class DbFixture:
    def __init__(self, host, name, user, password):
        self.host = host
        self.name = name
        self.user = user
        self.password = password
        self.connection = connect(host=host, database=name, user=user, password=password)

    def destroy(self):
        self.connection.close()