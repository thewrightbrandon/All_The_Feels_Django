from django.db import models
from django.utils import timezone

# Create your models here.

class Mood(models.Model):
    title = models.CharField(max_length=50)
    emotion = models.CharField(max_length=75)
    notes = models.TextField()
    created_at = models.DateField(auto_now_add=True)

class Comments(models.Model):
    mood = models.ForeignKey(Mood, null=True, on_delete=models.CASCADE, related_name='comments')
    name = models.CharField(max_length=250)
    body = models.TextField()
