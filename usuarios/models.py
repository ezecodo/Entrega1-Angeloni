from django.contrib.auth.models import User
from django.db import models
from ckeditor.fields import RichTextField


class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    profile_image = models.ImageField(upload_to='profile_images/', null=True, blank=True)
    bio = RichTextField(blank=True, null=True)
   
