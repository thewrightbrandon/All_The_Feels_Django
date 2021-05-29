from django.db import models
from django.utils import timezone

# Create your models here.

class Mood(models.Model):
    title = models.CharField(max_length=50)
    emotion = models.CharField(max_length=75)
    notes = models.TextField()
    created_at = models.DateField(auto_now_add=True)

class Comment(models.Model):
    name = models.CharField(max_length=150)
    comment = models.TextField()
