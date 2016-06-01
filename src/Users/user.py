from uuid import uuid4
from .group import Group
from django.db import models
from djangotoolbox.fields import EmbeddedModelField


class User(models.Model):
    class Meta:
        app_label = "SekPythonApi"
        db_table = 'users'
        
    id = models.UUIDField(primary_key=True, default=uuid4(), editable=False)
    first_name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=200)
    address = EmbeddedModelField('Address')
    group_id = models.ForeignKey(Group, on_delete=models.CASCADE, related_name='users')


class Address(models.Model):
    address_1 = models.CharField(max_length=1500)
    address_2 = models.CharField(max_length=1500, blank=True, null=True)
    city = models.CharField(max_length=50)
    state = models.CharField(max_length=5)
    zip_code = models.CharField(max_length=5)
