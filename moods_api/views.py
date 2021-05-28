from rest_framework import generics
from .serializers import MoodSerializer
from .serializers import CommentSerializer
from .models import Mood
from .models import Comment

# Create your views here.
class MoodList(generics.ListCreateAPIView):
    queryset = Mood.objects.all().order_by('id')
    serializer_class = MoodSerializer

class MoodDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Mood.objects.all().order_by('id')
    serializer_class = MoodSerializer

class CommentList(generics.ListCreateAPIView):
    queryset = Comment.objects.all().order_by('id')
    serializer_class = CommentSerializer

class CommentDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Comment.objects.all().order_by('id')
    serializer_class = CommentSerializer
