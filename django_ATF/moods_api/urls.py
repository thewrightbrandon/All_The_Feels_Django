from django.urls import path
from . import views

urlpatterns = [
    path('api/moods', views.MoodList.as_view(), name='mood_list'),
    path('api/moods/<int:pk>', views.MoodDetail.as_view(), name='mood_detail')
]
