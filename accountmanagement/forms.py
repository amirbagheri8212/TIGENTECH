from django.contrib.auth.forms import AuthenticationForm
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

# If you don't do this you cannot use Bootstrap CSS
class LoginForm(AuthenticationForm):
    username = forms.CharField(label="Username", max_length=30,
                               widget=forms.TextInput(attrs={'class': 'form-control', 'name': 'username'}))
    password = forms.CharField(label="Password", max_length=30,
                               widget=forms.TextInput(attrs={'class': 'form-control', 'name': 'password'}))
class SignUpForm(UserCreationForm):
    email = forms.EmailField(max_length=254)
    first_name = forms.CharField(label="First Name",max_length=40)
    last_name = forms.CharField(label="Last Name",max_length=50)
    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2', )
