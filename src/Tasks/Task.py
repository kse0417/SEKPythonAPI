from uuid import uuid4


class Task(object):
    def __init__(self):
        self.id = uuid4()
        #String
        self.title = None
        #String
        self.description = None
        #Date
        self.dueDate = None
        #User Type
        self.assignGroup = None
        # User
        self.assignedTo = None
        #
        self.priority = None
        # UUID - taskId
        self.parentTask = None
        # List<Task>
        self.subTasks = []
        # List<Task>
        self.dependencies = []