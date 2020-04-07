<<<<<<< HEAD
from django.contrib.auth.models import User
from django import forms
# from authapp.models import PizzaShop
from .models import Profile


class UserForm(forms.ModelForm):
    email = forms.CharField(max_length=100, required=True)
    password = forms.CharField(widget=forms.PasswordInput)
    class Meta:
        model = User
        fields = ('username', 'password', 'first_name',
                  'last_name', 'email')


class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
=======
from django.contrib.auth.models import User
from django import forms
# from authapp.models import PizzaShop
from .models import Profile


class UserForm(forms.ModelForm):
    email = forms.CharField(max_length=100, required=True)
    password = forms.CharField(widget=forms.PasswordInput)
    class Meta:
        model = User
        fields = ('username', 'password', 'first_name',
                  'last_name', 'email')


class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
>>>>>>> 41cab1c05f495a20062a33725f040476f3915cb5
        fields = ('number', 'quantity_of_workers', 'job', 'city')