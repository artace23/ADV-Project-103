from django import forms
from .models import TodoItem
from django.contrib.auth.forms import UserCreationForm, UserChangeForm, PasswordChangeForm
from django.contrib.auth.models import User

class AddTodoItemForm(forms.ModelForm):
    class Meta:
        model = TodoItem
        fields = ['title', 'description']
        
class DoneTodoForm(forms.Form):
    completed = forms.BooleanField(initial=True, required=False)

class UpdateTodoItemForm(forms.ModelForm):
    class Meta:
        model = TodoItem
        fields = ['title', 'completed', 'description']
        
class CreateUserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']
        
        
class EditProfileForm(UserChangeForm):
    email = forms.EmailField(widget=forms.EmailInput(attrs={'class': 'form-control'}))
    first_name = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'class': 'form-control'}))
    last_name = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'class': 'form-control'}))
    username = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'class': 'form-control'}))
    date_joined = forms.CharField(max_length=100, widget=forms.DateInput(attrs={'class': 'form-control', 'readonly': 'true', 'disable': 'true'}))
    
    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email','date_joined')
        
class PasswordChangingForm(PasswordChangeForm):
    old_password = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control', 'type': 'password'}))
    new_password1 = forms.CharField(max_length=100, widget=forms.PasswordInput(attrs={'class': 'form-control', 'type': 'password'}))
    new_password2 = forms.CharField(max_length=100, widget=forms.PasswordInput(attrs={'class': 'form-control', 'type': 'password'}))
    
    class Meta:
        model = User
        fields = ('old_password', 'new_password1', 'new_password2')