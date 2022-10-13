from django.urls import path
from todolist.views import *

app_name = 'todolist'

urlpatterns = [
    path('', show_todolist, name='show_todolist'),
    path('register/', user_register, name='user_register'),
    path('login/', user_login, name='user_login'),
    path('logout/', user_logout, name='user_logout'),
    path('create-task/', create_task, name='create_task'),
    path('delete-task/<int:id>/', delete_task, name='delete_task'),
    path('change-status/<int:id>/', change_status, name='change_status'),
    path('json/', get_todolist_json, name='get_todolist_json'),
    path('add/', add_task, name='add_task'),
]