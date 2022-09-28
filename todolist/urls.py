from django.urls import path
from todolist.views import user_register, user_login, user_logout, show_todolist, create_task

app_name = 'todolist'

urlpatterns = [
    path('', show_todolist, name='show_todolist'),
    path('register/', user_register, name='user_register'),
    path('login/', user_login, name='user_login'),
    path('logout/', user_logout, name='user_logout'),
    path('create-task/', create_task, name='create_task'),
]