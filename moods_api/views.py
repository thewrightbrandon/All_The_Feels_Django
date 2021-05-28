from rest_framework import generics
from .serializers import MoodSerializer
from .models import Mood
from .serializers import CommentsSerializer
from .models import Comments


# Create your views here.
class MoodList(generics.ListCreateAPIView):
    queryset = Mood.objects.all().order_by('id')
    serializer_class = MoodSerializer

class MoodDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Mood.objects.all().order_by('id')
    serializer_class = MoodSerializer

class CommentsList(generics.ListCreateAPIView):
    queryset = Comments.objects.all().order_by('id')
    serializer_class = CommentsSerializer

class CommentsDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Comments.objects.all().order_by('id')
    serializer_class = CommentsSerializer
