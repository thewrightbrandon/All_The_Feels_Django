from rest_framework import generics
from .serializers import MoodSerializer
from .models import Mood


# Create your views here.
class MoodList(generics.ListCreateAPIView):
    queryset = Mood.objects.all().order_by('id')
    serializer_class = MoodSerializer

class MoodDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Mood.objects.all().order_by('id')
    serializer_class = MoodSerializer
