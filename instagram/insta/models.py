from django.db import models

from django.contrib.auth.models import User

# Create your models here.
class Post(models.Model):
    postpic = models.ImageField(upload_to='post_images',default = 'logo.png')
    user = models.ForeignKey(User)
    caption = models.CharField(max_length = 250, blank=True)
    date = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.caption