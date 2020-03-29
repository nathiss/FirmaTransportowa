from django.db import models
from django.contrib.auth.models import User
from django.dispatch import receiver
from django.db.models.signals import post_save

from .person import Person


# https://simpleisbetterthancomplex.com/tutorial/2016/07/22/how-to-extend-django-user-model.html#onetoone
class Client(Person):
    class Meta:
        verbose_name = 'Client'
        verbose_name_plural = 'Clients'
    user = models.OneToOneField(User, on_delete=models.CASCADE)

@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, *args, **kwargs):
    if created:
        # pylint: disable=no-member
        Client.objects.create(user=instance)

@receiver(post_save, sender=User)
def save_user_profile(sender, instance, *args, **kwargs):
    instance.client.save()
