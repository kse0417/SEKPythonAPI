from uuid import uuid4
from django.db import models

PRIORITY = ((0, "Sky will fall"), (1, "I'll be mad"), (2, "Get it done"),(3, "Try to get it done"), (4, "We'll see"))


class Task(models.Model):
    class Meta:
        app_label = "SekPythonApi"
        db_table = 'tasks'

    id = models.UUIDField(primary_key=True, default=uuid4(), editable=False)
    title = models.CharField(max_length=200)
    description = models.CharField(max_length=1500, blank=True, default='')
    due_date = models.DateField(blank=True)
    priority = models.IntegerField(choices=PRIORITY, default=3)
    # TODO: Figure out one to many relationship for Django
    #           parentTask, subTasks, assignGroup
    # TODO: Figure out many to many relationship
    #           dependencies, assignTo
