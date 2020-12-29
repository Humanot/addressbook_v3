class Group:
    def __init__(self, id=None, name=None, header=None, footer=None):
        self.id = id
        self.name = name
        self.header = header
        self.footer = footer

    def __repr__(self):
        return f'{self.id}:{self.name}'

    def __eq__(self, other):
        return self.id == other.id and self.name == other.name