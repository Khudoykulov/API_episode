from django.urls import path, include
from .views import ContactViewSet
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register('contact', ContactViewSet, basename='contact')

app_name = 'main'

urlpatterns = [
    path('', include(router.urls)),
]
