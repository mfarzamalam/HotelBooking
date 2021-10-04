from django.shortcuts import redirect, render
from django.views import View
from .models import Hotel, Booking
from .forms import UserRegistrationForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required


# Create your views here.
class Index(View):
    def get(self, request):
        karachi = Hotel.objects.filter(city='Karachi')
        lahore = Hotel.objects.filter(city='Lahore')

        context = {'karachi':karachi, 'lahore':lahore}
        return render(request, 'app/index.html', context)


class UserRegister(View):
    def get(self, request):
        forms = UserRegistrationForm()
        context = {'forms':forms}

        return render(request, 'app/customerregistration.html', context)

    def post(self, request):
        forms = UserRegistrationForm(request.POST)
        if forms.is_valid():
            forms.save()
            messages.info(request, "Successfully Registerd!")
            forms = UserRegistrationForm()

        context = {'forms':forms}
        return render(request, 'app/customerregistration.html', context)


class HotelDetail(View):
    def get(self, request, pk):
        hotel = Hotel.objects.get(pk=pk)
        rooms = Hotel.objects.get(pk=pk)
        booked = Booking.objects.filter(hotel=pk)

        context = {'hotel':hotel, 'rooms':range(rooms.rooms+1), 'book':booked}
        return render(request, 'app/hoteldetail.html', context)


def add_to_cart(request):
    user     = request.user
    hotel_pk = request.GET.get('hotel_pk')
    room_no  = request.GET.get('room_no')
    hotel    = Hotel.objects.get(pk=hotel_pk)

    check_room_no = Booking.objects.filter(room_no=room_no, hotel=hotel).count()
    if check_room_no == 0:
        Booking(user=user, hotel=hotel, room_no=room_no).save()
        return redirect('/success')
    else:
        return redirect('/failed')


def success(request):
    return render(request, 'app/success.html')


def failed(request):
    return render(request, 'app/failed.html')