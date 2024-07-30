from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Photo(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    image = models.ImageField(upload_to='photos/')
    tags = models.CharField(max_length=90)
    likes = models.ManyToManyField(User, related_name='liked_photos')
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    bio = models.TextField(blank=True)
    profile_picture = models.ImageField(upload_to='profile_pictures',blank=True)

    def __str__(self):
        return self.user




