from django.shortcuts import render, redirect
from rest_framework.decorators import api_view
from rest_framework.response import Response


@api_view(['GET'])
def redirectToTodoList(request):
    return render(request, 'list.html')

def todoList(request):
    return render(request, 'list.html')

def handler404(request, exception):
    return render(request, '404.html')

