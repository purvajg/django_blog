'''
Adds tables created in the models.py to the admin(superuser) gui provided by
Django

Django has a builtin admin interface that reads metadata from your models,
such as fields, and lets you perform CRUD operations for free.

To be able to perform such operations, you need to register your models in the
admin.py file

The admin app is usually available under yoursite.com/admin, but you can also
change that in the urls.py file.
'''
from django.contrib import admin
from .models import Profile
# to register Profile model we first have to import the model

admin.site.register(Profile)
