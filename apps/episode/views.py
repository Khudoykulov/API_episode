from django.shortcuts import get_object_or_404
from rest_framework.response import Response
from rest_framework import generics, viewsets
from .models import Category, Tag, Episode, EpisodeLike, EpisodeComment
from rest_framework.permissions import IsAuthenticated, IsAuthenticatedOrReadOnly
from .permissions import IsAuthorOrReadOnly
from .filters import EpisodeFilter
from rest_framework import filters
import django_filters
from django_filters import rest_framework as filterset

from .serializers import (
    CategorySerializer,
    EpisodeSerializer,
    TagSerializer,
    EpisodeCommentSerializer,
    EpisodePostSerializer,
    EpisodeLikeSerializer
)


class CategoryAPIView(generics.ListAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    pagination_class = None


class TagAPIView(generics.ListAPIView):
    queryset = Tag.objects.all()
    serializer_class = TagSerializer
    pagination_class =None


class EpisodeAPIView(viewsets.ModelViewSet):
    queryset = Episode.objects.all()
    serializer_class = EpisodeSerializer
    serializer_post_class = EpisodePostSerializer
    permission_classes = [IsAuthorOrReadOnly]
    filter_backends = (filterset.DjangoFilterBackend, filters.SearchFilter)
    filterset_class = EpisodeFilter
    search_fields = ['title']

    def get_serializer_class(self):
        if self.request.method == 'GET':
            return super().get_serializer_class()
        return self.serializer_post_class


class EpisodeCommentAPIView(generics.ListCreateAPIView):
    #/episode/{episode_id}/comments/
    queryset = EpisodeComment.objects.all()
    serializer_class = EpisodeCommentSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]

    def get_serializer_context(self):
        ctx = super().get_serializer_context()
        episode_id = self.kwargs.get('episode_id')
        ctx['episode_id'] = episode_id
        return ctx

    def get_queryset(self):
        episode_id = self.kwargs.get('episode_id')
        qs = super().get_queryset()
        if episode_id:
            return qs.filter(episode_id=episode_id)
        return qs.none()


class EpisodeCommentDetailAPIView(generics.DestroyAPIView):
    #/episode/{episode_id}/comments/{pk}/
    queryset = EpisodeComment.objects.all()
    serializer_class = EpisodeCommentSerializer

    def get_queryset(self):
        episode_id = self.kwargs.get('episode_id')
        qs = super().get_queryset()
        if episode_id:
            return qs.filter(episode_id=episode_id)
        return qs.none()


class EpisodeLikeAPIView(generics.GenericAPIView):
    queryset = EpisodeLike.objects.all()
    serializer_class = EpisodeLikeSerializer
    permission_classes = [IsAuthenticated]

    def post(self, request, *args, **kwargs):
        """
            {
                "episode_id: 2"
            }
        """
        episode_id = request.data.get('episode_id')
        user_id = request.user.id
        get_object_or_404(Episode, id=episode_id)
        has_like = EpisodeLike.objects.filter(episode_id=episode_id, author_id=user_id)
        if has_like.exists():
            has_like.delete()
            return Response({'detail': 'Removed from liked list'})
        EpisodeLike.objects.create(episode_id=episode_id, author_id=user_id)
        return Response({'detail': 'Added to  liked list'})

