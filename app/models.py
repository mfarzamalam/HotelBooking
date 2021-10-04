from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class Customer(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    city = models.CharField(max_length=100)

    def __str__(self):
        return str(self.id)


class Hotel(models.Model):
    name      = models.CharField(max_length=100)
    address   = models.CharField(max_length=100)
    contact   = models.CharField(max_length=100)
    city      = models.CharField(max_length=100)
    rooms     = models.IntegerField()
    price     = models.IntegerField()
    hotel_img = models.ImageField(upload_to='hotel_img')

    def __str__(self):
        return str(self.name)


class Booking(models.Model):
    user     = models.ForeignKey(User, on_delete=models.CASCADE)
    hotel    = models.ForeignKey(Hotel, on_delete=models.CASCADE)
    room_no  = models.IntegerField()

    def __str__(self):
        return str(self.id)