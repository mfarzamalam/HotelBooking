from django.contrib import admin
from .models import (Customer, Hotel, Booking)


# Register your models here.
@admin.register(Customer)
class Customer(admin.ModelAdmin):
    list_display = ['id','user','name','city']


@admin.register(Hotel)
class Hotel(admin.ModelAdmin):
    list_display = ['id','name','address','contact','city','price','rooms','hotel_img']


@admin.register(Booking)
class Booking(admin.ModelAdmin):
    list_display = ['id','user','hotel','room_no']