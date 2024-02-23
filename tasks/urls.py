from django.urls import path
from .views import *

urlpatterns = [
    path('', home, name= 'home'),
    path('signup/', signup, name= 'signup'),
    path('Logout/', Logout, name= 'Logout'),
    path('createTask/', createTask, name= 'createTask'),
    path('login/', Login, name= 'Login'),
    path('tasks/', tasks, name= 'tasks'),
    path('tasks/<id>', editTask, name= 'editTask'),
    path('tasks/<id>/delete', deleteTask, name= 'deleteTask'),
    path('tasks/<id>/complete', completeTask, name= 'completeTask'),
    path('tasksComplete/', tasksComplete, name= 'tasksComplete'),
]