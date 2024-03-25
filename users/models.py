from django.db import models
from django.contrib.auth.models import User
from PIL import Image
# Create your models here.

class Profile(models.Model):
    user = models.OneToOneField(User,on_delete= models.CASCADE)
    bio = models.CharField(max_length=200, blank=True, null=True)
    # profile_pic = models.ImageField(default='default.png', upload_to = 'profile_pics', blank = True, null = True)
    is_teacher = models.BooleanField(default=False)

    objects = models.Manager()

    def __str__(self):
        return self.user.username + ' Profile'

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)


class Requirements(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE,)
    name = models.CharField(max_length=50)
    email = models.EmailField(max_length=254)
    phone_no = models.CharField(max_length=15)
    why = models.TextField(default = "")

    def __str__(self):
        return self.user.username