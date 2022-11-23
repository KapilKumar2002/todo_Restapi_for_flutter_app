from django.urls import path

from .views import CreateMission, ReadUpdateDeleteMission

urlpatterns = [
    path('', CreateMission.as_view()),
    path('<int:pk>/', ReadUpdateDeleteMission.as_view())
]