# this file is created for the purpose of making custom forms.
# In users->registration.html the form that we are  using is given by django.
# That form does not have the 'email' field.
# Hence, to make that form custom we need to create a new form which will inherit
# the form given by djnago(UserCreationForm)

from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import Profile

class UserRegistrationForm(UserCreationForm):#inherits form UserCreationForm
    email = forms.EmailField() #default is 'required=true'. Hence no need to put anything

    class Meta:
        model = User
        # the model  that we want this form to interact with. Model is going
        # to be user because whenever this form validates its gonna create a new
        # user
        # form.save() will save the form to the user model
        fields = ['username', 'email', 'password1', 'password2']
        # field that would be displayed in the order which they should appear


# updates username and email:
class UserUpdateForm(forms.ModelForm):
    email = forms.EmailField()
    class Meta:
        model = User
        fields = ['username', 'email']


# updates profile photo:
class ProfileUpdateForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['image']
