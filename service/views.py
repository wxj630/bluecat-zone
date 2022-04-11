from django.shortcuts import render

# Create your views here.
from rest_framework import viewsets

from service.models import Service
from service.serializers import ServiceSerializer,ServiceDetailSerializer
from service.permissions import IsOwnerOrReadOnly

from rest_framework import filters

class ServiceViewSet(viewsets.ModelViewSet):
    queryset = Service.objects.all()
    serializer_class = ServiceSerializer
    permission_classes = [IsOwnerOrReadOnly]

    filter_backends = [filters.SearchFilter]
    search_fields = ['title']

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)

    def get_serializer_class(self):
        if self.action == 'list':
            return ServiceSerializer
        else:
            return ServiceDetailSerializer

