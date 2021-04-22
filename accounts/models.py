from django.db import models
from django.contrib.auth.models import User
from django.utils.text import slugify
from django.db.models.signals import post_save
# Create your models here.

# create profile model 

class Profile(models.Model):
    user = models.OneToOneField(User , on_delete=models.CASCADE)
    username = models.CharField(max_length=20, blank=True , null=True)
    first_name = models.CharField(max_length=30, blank=True , null=True)
    last_name = models.CharField(max_length=40, blank=True , null=True)
    address = models.CharField(max_length=40, blank=True , null=True)
    email = models.EmailField(max_length=50, blank=True , null=True)
    image = models.ImageField(upload_to='profile', blank=True , null=True)
    entered_date = models.DateTimeField(auto_now_add=True)
    sulg = models.SlugField(max_length=20 , blank=True , null=True)

    def __str__(self):
        return str(self.user.username)

def save(self, *args, **kwargs):
    self.slug = slugify(self.username)
    super(Profile, self).save(*args, **kwargs)



def create_profile(sender , created , instance ,**kwargs):
    if created:
        Profile.objects.create(user=instance)

post_save.connect(create_profile, sender=User)
