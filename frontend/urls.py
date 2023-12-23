from django.urls import path
from . import views
from django.contrib.auth.decorators import login_required
from django.conf.urls import handler404

urlpatterns = [
    path("", login_required(views.redirectToTodoList, login_url='/api/account/login/'), name="redirectToTodoList"),
    path("todo-list/", login_required(views.todoList, login_url='/api/account/login/'), name="todoList"),
]

handler404 = 'finalProject.views.handler404'