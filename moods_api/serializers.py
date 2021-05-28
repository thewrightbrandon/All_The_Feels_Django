from rest_framework import serializers
from .models import Mood
from .models import Comment

class MoodSerializer(serializers.ModelSerializer):
    class Meta:
        model = Mood
        fields = ('id', 'title', 'emotion', 'notes', 'created_at',)

class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = ('id', 'name', 'comment', 'mood_id')
