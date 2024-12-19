from django.urls import path
from . import views

app_name = 'tareas'

urlpatterns = [
    path('',views.home, name = 'home'),
    path('tarea_detail/<pk>',views.detail_tarea, name ='detail-tarea'),
    path('edit_tarea/<pk>',views.edit_tarea, name ='tareaEdit'),
]