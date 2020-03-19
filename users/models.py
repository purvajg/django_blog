# Any change to models have to be changed in the data base too
# Every class in models has to inherit models.Model
# Models are tables in database. Every field is the attribute of the  table
from django.db import models
from django.contrib.auth.models import User


# extending the existing user model provided by django

# Create profile page for users with profile  picture
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    # creating a one to one relationship for each user

    image = models.ImageField(default='default.jpg', upload_to='profile_pics')

    # creating a image field which has a default image and it gets uploaded to
    # a default folder

    def __str__(self):
        return f'{self.user.username} Profile'

    def set_user(self, user):
        self.user = user

    # creating a dunder_str method so that when we print this out, it will dispaly
    # how  we want it to display
    # if we  dont have a dunder_str method then anytime we print a profile
    # then  its gonna say 'profile object', but we want it to be more desprictive
    # than that, and to do it we need to tell it how to print it out
    # return f'{self.user.username} Profile' ==> it would print out the username
    # then Profile eg. Purva Profile i.e it makes the printig out better to read
