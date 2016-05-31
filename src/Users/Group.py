from uuid import uuid4
from django.db import models


class Group(models.Model):
    class Meta:
        app_label = "SekPythonApi"
        db_table = 'groups'

    id = models.UUIDField(primary_key=True, default=uuid4(), editable=False)
    title = models.CharField(max_length=200)
    description = models.CharField(max_length=1500, blank=True, default='')
    # privilege = []
