from rest_framework import generics
from . import models
from . import serialisers

class OverView(generics.ListAPIView):
    queryset = models.ToDo.objects.all()
    serializer_class = serialisers.ToDoSerialiser

class CreateView(generics.CreateAPIView):
    queryset = models.ToDo.objects.all()
    serializer_class = serialisers.ToDoSerialiser

class UpdateView(generics.UpdateAPIView):
    queryset = models.ToDo.objects.all()
    serializer_class = serialisers.ToDoSerialiser

class DeleteView(generics.DestroyAPIView):
    queryset = models.ToDo.objects.all()
    serializer_class = serialisers.ToDoSerialiser
