
from typing import Any
from django.db import models
from django.shortcuts import render, redirect

from rest_framework.decorators import api_view, authentication_classes, permission_classes

from rest_framework.permissions import IsAuthenticated

from rest_framework.authentication import SessionAuthentication, BasicAuthentication

from rest_framework.response import Response

from .serializers import TodoItemSerializer

from .models import TodoItem

from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.views import PasswordChangeView
from .forms import CreateUserForm, EditProfileForm, PasswordChangingForm
from django.urls import reverse_lazy
from django.views import generic

from django.contrib.auth.decorators import login_required

@api_view(['GET'])
def redirectToTodoList(request):
    return render(request, 'list.html')

@login_required
@api_view(['GET'])
def todoList(request):
    todos = TodoItem.objects.filter(user=request.user).all().order_by('-id')
    serializer = TodoItemSerializer(todos, many=True)
    
    return Response(serializer.data)

@login_required
@api_view(['POST'])
@authentication_classes([SessionAuthentication, BasicAuthentication])
@permission_classes([IsAuthenticated])
def todoCreate(request):
    serializer = TodoItemSerializer(data=request.data, context={'request': request})

    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    else:
        return Response(serializer.errors, status=400)

@login_required
@api_view(['POST'])
@authentication_classes([SessionAuthentication, BasicAuthentication])
@permission_classes([IsAuthenticated])
def todoUpdate(request, pk):
    todo = TodoItem.objects.filter(user=request.user).get(id=pk)
    serializer = TodoItemSerializer(instance=todo, data=request.data, context={'request': request})
    
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    else:
        return Response(serializer.errors, status=400)

@login_required
@api_view(['DELETE'])
def todoDelete(request, pk):
    todos = TodoItem.objects.get(id=pk)
    todos.delete()
    return Response("Item Successfully Deleted")

def loginPage(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('todoList')
        else:
            messages.error(request, 'Invalid login credentials')

    return render(request, 'login.html')

def logoutUser(request):
    logout(request)
    return redirect('login')

def registerPage(request):
    form = CreateUserForm()
    
    if request.method == 'POST':
        form = CreateUserForm(request.POST)
        if form.is_valid():
            form.save()
            user = form.cleaned_data.get('username')
            messages.success(request, 'Account was created for ' + user)
            
            return redirect('login')
    
    context = {'form':form}
    return render(request, 'register.html', context)

class UserEditView(generic.UpdateView):
    form_class = EditProfileForm
    template_name = 'profile.html'
    success_url = reverse_lazy('todoList')
    
    def get_object(self):
        return self.request.user
    
class PasswordsChangeView(PasswordChangeView):
    form_class = PasswordChangingForm
    success_url = reverse_lazy('password_success')
    
def password_success(request):
    return render(request, 'password_success.html', {})

def handler404(request, exception):
    return render(request, '404.html')