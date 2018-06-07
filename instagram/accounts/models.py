from django.db import models
from django.db.models.signals import post_save
from django.contrib.auth.models import User


# Create your models here.
class UserProfile(models.Model):
    user = models.OneToOneField(User)
    name = models.CharField(max_length = 100, default = 'My Name')
    bio = models.CharField(max_length = 100, default = 'A little about me!')
    profpic = models.ImageField(upload_to='profile_images',default = 'logo.png')
    website = models.URLField()

    def create_profile(sender, **kwargs):
        if kwargs['created']:
            user_profile = UserProfile.objects.create(user=kwargs['instance'])

    post_save.connect(create_profile, sender=User)

    def __str__(self):
        return self.name