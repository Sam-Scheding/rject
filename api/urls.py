from django.urls import path
from . import views

urlpatterns = [
    path('todo/', views.OverView.as_view(), name='overview'),
    path('todo/create/', views.CreateView.as_view(), name='create'),
    path('todo/update/<int:pk>/', views.UpdateView.as_view(), name='update'),
    path('todo/delete/<int:pk>/', views.DeleteView.as_view(), name='delete'),

]
