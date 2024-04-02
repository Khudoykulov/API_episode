from django.urls import path, include
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
router.register('actions', EpisodeAPIView)
urlpatterns = [
    path('category/list/', CategoryAPIView.as_view()),
    path('tags/list/', TagAPIView.as_view()),
    path('<int:episode_id>/comments/', EpisodeCommentAPIView.as_view(),),
    path('<int:episode_id>/comments/<int:pk>/', EpisodeCommentDetailAPIView.as_view(),),
    path('like/', EpisodeLikeAPIView.as_view(),),
    path('', include(router.urls))
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