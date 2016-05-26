from uuid import uuid4


class User(object):
    def __init__(self):
        self.id = uuid4()
        self.firstName = None
        self.lastName = None
        self.relation = None
        self.address = None
        self.userType = None
        self.seating = None
