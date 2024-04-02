from django.urls import path
from rest_framework.routers import DefaultRouter
from .views import (
    EpisodeAPIView,
    CategoryAPIView,
    TagAPIView,
    EpisodeLikeAPIView,
    EpisodeCommentAPIView,
    EpisodeCommentDetailAPIView
)
app_name = 'episode'


router = DefaultRouter()
urlpatterns = [
    path('category/list/', CategoryAPIView.as_view()),
    path('tags/list/', TagAPIView.as_view()),
    path('comment/list-create/', EpisodeCommentAPIView.as_view(),)
]


"""
Episode:
    -list
    -detail
    -create
    -delete
    -update
Category
    _list
Tag:
    -list

EpisodeComment:
    -list
    -create
    -delete

EpisodeLike
    -like
    -dislike    
"""