from .models import Profile
from django.contrib.auth.models import User

#https://docs.djangoproject.com/en/5.2/search/?q=django.db.models.signals+
#https://docs.djangoproject.com/en/5.2/search/?q=django.dispatch+receiver
from django.db.models.signals import post_save # 
from django.dispatch import receiver

@receiver(post_save, sender=User)
def post_save_create_profile(sender, instance, created, **kwargs):
    """Signal to create a Profile instance whenever a new user is created
    Arguments:
        sender: The model class.(User)
        instance: The actual instance being saved. (Profile)
        created: A boolean; True if a new record was created.
    """

    print(f"sender: {sender}")
    print(f"instance: {instance}")  #The actual instance being saved.
    print(f"created: {created}")
    if created:
        Profile.objects.create(user=instance)