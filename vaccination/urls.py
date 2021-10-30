from django.urls import path
from django.views.decorators.csrf import csrf_exempt

from . import views

urlpatterns = [
    path('login', csrf_exempt(views.Login.as_view()), name='login'),
    path('users', csrf_exempt(views.User.as_view()), name='users'),
    path('users/<int:id>', csrf_exempt(views.User.as_view()), name='users'),
    path('hospital', csrf_exempt(views.Hospital.as_view()), name='hospital'),
    path('hospital/<int:id>', csrf_exempt(views.Hospital.as_view()), name='hospital'),
    path('bookings', csrf_exempt(views.Booking.as_view()), name='bookings'),
    path('bookings/<int:bookingId>', csrf_exempt(views.Booking.as_view()), name='bookings'),
    path('bookings/user/<int:userId>', csrf_exempt(views.UserBookings.as_view()), name='userBookings'),
    path('bookingTypes', csrf_exempt(views.BookingType.as_view()), name='bookingTypes'),
    path('suppliers', csrf_exempt(views.Supplier.as_view()), name='suppliers'),
    path('volunteers', csrf_exempt(views.Volunteers.as_view()), name='volunteers'),
    path('insertion', views.Insertion, name='insertion'),
]