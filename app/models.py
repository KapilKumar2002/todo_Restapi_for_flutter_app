from django.db import models

# Create your models here.
class DailyMission(models.Model):
    task = models.CharField(max_length=100)
    taskdesc = models.CharField(max_length=200)
    # date = models.DateTimeField(auto_now_add=True)


    def __str__(self):
        return self.task