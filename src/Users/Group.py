from uuid import uuid4


class Group(object):
    def __init__(self):
        self.id = uuid4()
        self.title = None
        self.description = None
        # List<User>
        self.users = []
        # List
        self.privilege = []