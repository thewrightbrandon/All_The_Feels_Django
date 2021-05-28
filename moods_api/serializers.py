from rest_framework import serializers
from .models import Mood
from .models import Comments

class MoodSerializer(serializers.ModelSerializer):
    class Meta:
        model = Mood
        fields = ('id', 'title', 'emotion', 'notes', 'created_at',)

class CommentsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comments
        fields = ('id', 'mood', 'name', 'body',)
