import datetime
from django.db import models
from django.contrib.auth.models import User
from django.conf import settings
from django.utils import timezone
from django.forms import ModelForm



class Address(models.Model):
    postal_code = models.IntegerField()
    city = models.CharField(max_length=120)
    street_address = models.CharField(max_length=120)
    country = models.CharField(max_length=120)

    def __str__(self): #toString-metode, tittelen printes hvis man printer objektet
        return self.street_address + " - " + str(self.postal_code).zfill(4) + ", " + self.city

    class Meta:
        verbose_name = "Address"
        verbose_name_plural = "Addresses"


class Phase(models.Model):
    title = models.CharField(max_length=120)
    def __str__(self):
        return self.title;

class Tag(models.Model):
    title = models.CharField(max_length=120)
    def __str__(self):
        return self.title;

class Startup(models.Model):
    bio = models.TextField(max_length=500, blank=True, null=True)
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    address = models.OneToOneField(Address, on_delete=models.CASCADE)
    employees = models.IntegerField()
    phase = models.ForeignKey(Phase, blank=True, default=1, on_delete=models.CASCADE)
    tags = models.ManyToManyField(Tag, blank=True)
    image = models.ImageField(upload_to='images/', default='no-image.png')

    def __str__(self): #toString-metode, tittelen printes hvis man printer objektet
        return self.user.first_name


class Person(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    bio = models.TextField(max_length=500, blank=True, null=True)
    address = models.OneToOneField(Address, on_delete=models.CASCADE, null=True)

    def __str__(self): #toString-metode, tittelen printes hvis man printer objektet
        return self.user.first_name


class Investor(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    bio = models.TextField(max_length=500, blank=True, null=True)

    def __str__(self): #toString-metode, tittelen printes hvis man printer objektet
        return self.user.first_name


class Advert(models.Model):
    title = models.CharField(max_length=120)
    startup = models.ForeignKey(Startup, default=1, on_delete=models.CASCADE)
    deadline = models.DateField()
    available_positions = models.IntegerField()
    description = models.TextField()

    def __str__(self): #toString-metode, tittelen printes hvis man printer objektet
        return self.title

    def almost_deadline(self): #returnerer true dersom vi det er 3 eller mindre dager til deadline
        self.deadline <= timezone.now() + datetime.timedelta(days=3)

class ContentType(models.Model):
    title = models.CharField(max_length=120)
    def __str__(self):
        return self.title;

class Content(models.Model):
    title = models.CharField(max_length=120)
    type = models.ForeignKey(ContentType, default=1, on_delete=models.CASCADE)
    text = models.TextField(max_length=1500, blank=True, null=True)
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    released = models.DateTimeField(auto_now=True)
    event_datetime = models.DateTimeField(blank=True, null=True)
    image = models.ImageField(upload_to='images/', default='no-image.png')

    def __str__(self):
        return str(self.type) + ": " + self.title;
