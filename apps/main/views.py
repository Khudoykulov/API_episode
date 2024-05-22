from rest_framework.viewsets import ModelViewSet

from .serializers import ContactSerializer
from .models import Contact


class ContactViewSet(ModelViewSet):
    queryset = Contact.objects.all()
    serializer_class = ContactSerializer


