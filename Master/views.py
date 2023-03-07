from django.shortcuts import render
from rest_framework import generics
from Master.models import Gender
from Master.serializers import GenderMasterSerializer
# Create your views here.
class GenderList(generics.ListCreateAPIView):
    queryset = Gender.objects.all()
    serializer_class = GenderMasterSerializer