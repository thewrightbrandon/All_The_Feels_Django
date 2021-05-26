from django.db import models

# Create your models here.

class Mood(models.Model):
    title = models.CharField(max_length=50)
    emotion = models.CharField(max_length=75)
    notes = models.TextField()
    created_at = models.DateField(auto_now_add=True)
