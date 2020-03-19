# signals are used to identify when an action is taking place.
# eg: when a user signs up as a new user, we dont want him to redo the profile
# creation, insted we want to get a signals which would tell us that a new user
# has signed up and so now his profile needs to be created.
# post_save is used when the signal is to be given after the save method is called
# pre_save also exits which is used before calling save method
# We have called the save method in user.views.profile where form.save() is used
from django.db.models.signals import post_save
from django.contrib.auth.models import User
#this  will be our  sender
from django.dispatch import receiver
from .models import Profile

@receiver(post_save, sender=User)
def create_profile(sender, instance, created, **kwargs):
    try:
        instance.profile.save()
    except :# if created:
        Profile.objects.create(user=instance)
    # Try catch is added because: when we  create a OneToOne relation field in
    # models.py.
    # Here it thus means that although every Profile has a related user, not every
    # user has a Profile. It is possible that there are Users for which no Profile
    # exists.
    # If you thus query some_user.profile there are two scenario's that can unfold:
    # there is a related Profile object that is the fetched, and returned; or
    # there is no such object, and then it raises a RelatedObjectDoesNotExist error.
    # So you probably have a user for which there is no profile.
    # the error happens on the line instance.profile.save().


@receiver(post_save, sender=User)
def save_profile(sender, instance, **kwargs):
    instance.profile.save()
