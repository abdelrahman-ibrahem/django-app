from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm




class RegisterForm(UserCreationForm):
    username = forms.CharField(label="username")
    email = forms.EmailField(label="Email")
    password1 = forms.CharField(label="Enter the password" , widget=forms.PasswordInput())
    password2 = forms.CharField(label="Enter the password" , widget=forms.PasswordInput())
    class Meta:
        model = User
        fields = ['username' , 'email' , 'password1' , 'password2']



class LoginForm(forms.ModelForm):
    username = forms.CharField(label="username")
    password = forms.CharField(label="password" , widget=forms.PasswordInput())
    class Meta:
        model = User
        fields = ['username' , 'password']



class UpdateProfile(forms.ModelForm):
    username = forms.CharField(label='username')
    first_name = forms.CharField(label='First name')
    last_name = forms.CharField(label='Last name')
    email = forms.EmailField(label='Email')
    class Meta:
        model = User
        fields = ['username' , 'first_name' , 'last_name' , 'email']