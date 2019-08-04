from rest_framework.serializers import ModelSerializer
from . import models

class ToDoSerialiser(ModelSerializer):
  class Meta:
    model = models.ToDo
    fields = [ 'text', ]
