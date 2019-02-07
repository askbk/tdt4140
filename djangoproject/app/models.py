import datetime
from django.db import models
from django.contrib.auth.models import User
from django.conf import settings
from django.utils import timezone

# Create your models here.
class Advert(models.Model):
    title = models.CharField(max_length=120)
    company = models.ForeignKey(settings.AUTH_USER_MODEL, default=1, on_delete=models.CASCADE)
    deadline = models.DateTimeField()
    available_positions = models.IntegerField()
    description = models.TextField()

    def __str__(self): #toString-metode, tittelen printes hvis man printer objektet
        return self.title

    def almost_deadline(self): #returnerer true dersom vi det er 3 eller mindre dager til deadline
        self.deadline <= timezone.now() + datetime.timedelta(days=3)
