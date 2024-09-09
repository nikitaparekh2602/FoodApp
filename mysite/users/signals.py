from django.db.models.signals import post_save # because we want to get signals when the user data is saved
from django.contrib.auth.models import User
from django.dispatch import receiver # It will recieve the send singnal and it will perform some action
from .models import Profile


@receiver(post_save,sender=User) # recieve that signals
def build_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)

@receiver(post_save,sender=User)
def save_profile(sender, instance, **kwargs):
    instance.profile.save()







