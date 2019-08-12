from rest_framework import generics
from . import models
from . import serialisers

# /api/todo
class OverView(generics.ListAPIView):
    queryset = models.ToDo.objects.all()
    serializer_class = serialisers.ToDoSerialiser

# /api/todo/create
class CreateView(generics.CreateAPIView):
    queryset = models.ToDo.objects.all()
    serializer_class = serialisers.ToDoSerialiser

# /api/todo/update
class UpdateView(generics.UpdateAPIView):
    queryset = models.ToDo.objects.all()
    serializer_class = serialisers.ToDoSerialiser

# /api/todo/delete
class DeleteView(generics.DestroyAPIView):
    queryset = models.ToDo.objects.all()
    serializer_class = serialisers.ToDoSerialiser
