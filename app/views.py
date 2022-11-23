from rest_framework import generics

# Create your views here.
from .models import DailyMission
from .serializers import TodoSerializer


class CreateMission(generics.ListCreateAPIView):
    queryset = DailyMission.objects.all()
    serializer_class = TodoSerializer


class ReadUpdateDeleteMission(generics.RetrieveUpdateDestroyAPIView):
    queryset = DailyMission.objects.all()
    serializer_class = TodoSerializer