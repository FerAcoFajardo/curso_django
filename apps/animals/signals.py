from django.dispatch import receiver
from django.db.models.signals import post_save

from .models import Animal

@receiver(post_save, sender=Animal)
def say_hello(sender, instance, created, **kwargs):
    if created:
        print(f'Hello {instance.nombre}')
    # instance.save()
