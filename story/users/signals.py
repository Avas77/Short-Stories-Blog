from django.db.models.signals import post_save #when the user saves the info the signal is fires
from django.contrib.auth.models import User #this is the signal sender
from django.dispatch import receiver
from .models import Profile

@receiver(post_save,sender=User)
def create_profile(sender,instance,created,**kwargs):
	if created:
		Profile.objects.create(user=instance)

@receiver(post_save,sender=User)
def save_profile(sender,instance,**kwargs):
	instance.profile.save()
		