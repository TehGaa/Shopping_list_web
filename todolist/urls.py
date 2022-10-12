from django.urls import path
from todolist.views import show_todolist, register, login_user, logout_user, new_task, change_status, delete_task, json, add

app_name = 'todolist'

urlpatterns = [
    path('', show_todolist, name = 'show_todolist'),
    path('register/', register, name = 'register'),
    path('login/', login_user, name = 'login_user'),
    path('logout/', logout_user, name = 'logout_user'),
    path('add/', add, name = 'add'),
    path('create-task/', new_task, name = 'create-task'),
    path('change-status/', change_status, name = 'change-status'),
    path('delete/<str:id>', delete_task, name = 'delete'),
    path('json/', json, name = 'json'),
]