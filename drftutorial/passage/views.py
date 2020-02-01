from django.shortcuts import render
from passage.models import Passage
from passage.serializers import PassageSerializer
from rest_framework import viewsets

# Create your views here.
class PassageViewSet(viewsets.ModelViewSet):
    """

    """
    queryset = Passage.objects.all().order_by('-add_time')
    serializer_class = PassageSerializer

