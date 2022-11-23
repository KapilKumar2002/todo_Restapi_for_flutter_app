from rest_framework import serializers
from .models import DailyMission


class TodoSerializer(serializers.ModelSerializer):
    class Meta:
        model = DailyMission
        fields = '__all__'
