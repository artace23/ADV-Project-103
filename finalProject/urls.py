from django.urls import path
from . import views
from django.contrib.auth.decorators import login_required
from django.conf.urls import handler404

urlpatterns = [
    path("", login_required(views.redirectToTodoList, login_url='/api/account/login/'), name="redirectToTodoList"),
    path("view-todo/", login_required(views.todoList, login_url='/api/account/login/'), name="view-todo"),
    path("todo-create/", login_required(views.todoCreate, login_url='/api/account/login/'), name="todo-create"),
    path("todo-update/<str:pk>/", login_required(views.todoUpdate, login_url='/api/account/login/'), name="todo-update"),
    path("todo-delete/<str:pk>/", login_required(views.todoDelete, login_url='/api/account/login/'), name="todo-delete"),
    path('account/login/', views.loginPage, name='login'),
    path('account/logout/', views.logoutUser, name='logout'),
    path('account/register/', views.registerPage, name='register'),
    path('account/update-profile/', login_required(views.UserEditView.as_view(), login_url='/api/account/login/'), name='update-profile'),
    path('<int:uid>/password/', login_required(views.PasswordsChangeView.as_view(template_name='change-password.html'), login_url='/api/account/login/')),
    path('password_success/', login_required(views.password_success, login_url='/api/account/login/'), name = 'password_success'),
]

handler404 = 'finalProject.views.handler404'
