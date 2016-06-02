from uuid import uuid4


class Event(object):
    def __init__(self):
        self.id = uuid4()
        self.date = None
        # List <User>
        self.inviteList = []
        # List <User>
        self.yesList = []
        # List <User>
        self.noList = []
        # List <UserType>
        self.visibility = []
        #String
        self.title = None
        #String
        self.description = None
        #String
        self.location = None
        # String
        self.address = None
        # String
        self.notes = None
