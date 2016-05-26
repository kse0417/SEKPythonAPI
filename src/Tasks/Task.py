from uuid import uuid4
from django.db import models

PRIORITY = [("Sky will fall", 0), ("I'll be mad", 1), ("Get it done", 2),("Try to get it done", 3), ("We'll see", 4)]


class Task(models.Model):
    class Meta:
        app_label = "SekPythonApi"

    id = models.UUIDField(primary_key=True, default=uuid4(), editable=False)
    title = models.CharField(max_length=200)
    description = models.CharField(max_length=1500, blank=True, default='')
    dueDate = models.DateField(blank=True)
    priority = models.IntegerField(choices=PRIORITY, default=3)
    # TODO: Figure out one to many relationship for Django
    #           parentTask, subTasks, assignGroup
    # TODO: Figure out many to many relationship
    #           dependencies, assignTo
