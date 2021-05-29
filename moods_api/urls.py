from django.urls import path
from . import views

urlpatterns = [
    path('api/moods', views.MoodList.as_view(), name='mood_list'),
    path('api/moods/<int:pk>', views.MoodDetail.as_view(), name='mood_detail'),
    path('api/comments', views.CommentsList.as_view(), name='comments_list'),
    path('api/comments/<int:pk>', views.CommentsDetail.as_view(), name='comments_detail'),
]
