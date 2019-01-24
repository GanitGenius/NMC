from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User


class Schedule(models.Model):
    uid = models.ForeignKey(User, on_delete=models.CASCADE)
    hr = models.IntegerField()
    mn = models.IntegerField()
    date_added = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return str(self.hr) + " " + str(self.mn)

