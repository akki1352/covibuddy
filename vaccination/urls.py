from django.urls import path
from django.views.decorators.csrf import csrf_exempt

from . import views

urlpatterns = [
    path('login', csrf_exempt(views.Login.as_view()), name='login'),
    path('users', csrf_exempt(views.User.as_view()), name='users'),
    path('users/<uuid:id>', csrf_exempt(views.User.as_view()), name='users'),
    path('hospital', csrf_exempt(views.Hospital.as_view()), name='hospital'),
    path('hospital/<uuid:id>', csrf_exempt(views.Hospital.as_view()), name='hospital'),
    path('bookings', csrf_exempt(views.Booking.as_view()), name='bookings'),
    path('bookings/<uuid:bookingId>', csrf_exempt(views.Booking.as_view()), name='bookings'),
    path('bookings/user/<uuid:userId>', csrf_exempt(views.UserBookings.as_view()), name='userBookings'),
    path('bookingTypes', csrf_exempt(views.BookingType.as_view()), name='bookingTypes'),
    path('vaccineTypes', views.VaccineTypes, name='vaccineTypes'),
    path('vaccineCentres', views.VaccineCentres, name='vaccineCentres'),
]