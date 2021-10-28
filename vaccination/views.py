import json
from json.decoder import JSONDecodeError
from django.core.checks import messages
from django.http import response
from django.http.response import HttpResponseForbidden, HttpResponseNotModified, HttpResponseServerError
from django.shortcuts import render, resolve_url
from django.http import HttpResponse, JsonResponse, HttpResponseBadRequest
from django.views import View
from django.views.decorators.csrf import ensure_csrf_cookie
from vaccination.models import Bookings, BookingsType, Hospitals, VaccineType, VaccineCentre, Users
from django.db.utils import IntegrityError
from datetime import datetime

class Login(View):

    def post(self, request):
        body = json.loads(request.body)
        email_ = body.get('email', None)
        password_ = body.get('password', None)
        try:
            user = Users.objects.get(email=email_, password=password_)
            response = {
                'user':{
                    'id': user.id,
                    'name': user.name,
                    'email': user.email,
                    'type': user.type,
                    'contact': user.contact
                },
                'message': 'success' 
            }
            return JsonResponse(response, content_type='application/json')
        except Users.DoesNotExist as e:
            return HttpResponse('Unauthorized', status=401)
        except Exception as e:
            print(e)
            return HttpResponseServerError('Server Error Occured')

class User(View):

    def get(self, request, *args, **kwargs):
        id = kwargs.get('id', None)
        try:
            if id == None:
                users = Users.objects.all()
                response = {
                    'Users': list(users.values()),
                    'message': 'success' 
                }
                return JsonResponse(response, content_type='application/json')
            else:
                user = Users.objects.get(id=id)
                response = {
                    'hospital':{
                        'id': user.id,
                        'name': user.name,
                        'email': user.email,
                        'contact': user.contact
                    },
                    'message': 'success' 
                }
                return JsonResponse(response, content_type='application/json')
        except Users.DoesNotExist as e:
            return HttpResponse('User details does not exist', status=401)
        except Exception as e:
            return HttpResponseServerError('Server Error Occured')
    
    def post(self, request):
        body = json.loads(request.body)
        name = body.get('name', None)
        email = body.get('email', None)
        password = body.get('password', None)
        type = body.get('type', None)
        contact = body.get('contact', None)
        try:
            user = Users.objects.create(name=name, email=email, password=password, type=type, contact=contact)
            resp = {
                'user':{
                    'id': user.id,
                    'name': user.name,
                    'email': user.email,
                },
                'message': 'success' 
            }
            response = JsonResponse(resp)
            response.headers['Access-Control-Allow-Origin'] = '*'
            response.headers['Access-Control-Allow-Methods'] = 'PUT, GET, POST, DELETE, OPTIONS'
            response.headers['Access-Control-Allow-Headers'] = 'Origin, Accept, Content-Type, X-Requested-With, X-CSRF-Token'
            response.headers['Content-Type'] = "text/html; charset=utf-8"
            return response
        except IntegrityError as ite:
            return HttpResponseForbidden("Email Id already exists")
        except Exception as e:
            return HttpResponseServerError("Some Error occured")

    def put(self, request):
        body = json.loads(request.body)
        name = body.get('name', None)
        email = body.get('email', None)
        password = body.get('password', None)
        type = body.get('type', None)
        contact = body.get('contact', None)
        try:
            user = Users.objects.filter(email=email).update(name=name, contact=contact)
            print(body, user)
            return HttpResponse("User Updated Successfully.")
        except Exception as e:
            print(e)
            return HttpResponseServerError('Some Error occured!')

    def delete(self, request):
        body = json.loads(request.body)
        id = body.get('id', None)
        try:
            Users.objects.filter(id=id).delete()
            response = {
                'message': 'User details deleted successfully' 
            }
            return JsonResponse(response, content_type='application/json')
        except Exception as e:
            print(e)
            return HttpResponseServerError('Server Error Occured')

class Booking(View):

    def get(self, request, *args, **kwargs):
        bookingId = kwargs.get('bookingId', None)
        try:
            if bookingId:
                booking = Bookings.objects.get(id=bookingId)
                print(booking)
                response = {
                    'bookingId': booking.id,
                    'userId': booking.userId,
                    'hospitalId': booking.hospitalId,
                    'bookingType': booking.bookingType,
                    'bookingDate': booking.bookingDate,
                }
                return JsonResponse(response)
            else:
                bookings = Bookings.objects.all()
                response = {
                    'bookings': list(bookings.values())
                }
                return JsonResponse(response)
        except Exception as e:
            print(e)
            return HttpResponseServerError("Some server error occured")

    def post(self, request):
        body = json.loads(request.body)
        userId = body.get('user_id', None)
        hospitalId = body.get('hospital_id', None)
        bookingType = body.get('booking_type', None)
        bookingDate = body.get('booking_date', None)
        try:
            booking = Bookings.objects.create(userId=userId, hospitalId=hospitalId, bookingType=bookingType, bookingDate=datetime.strptime(bookingDate, '%Y-%m-%dT%H:%M'))
            response = {
                'bookingId': booking.id,
                'userId': booking.userId,
                'hospitalId': booking.hospitalId
            }
            return JsonResponse(response)
        except Exception as e:
            print(e)
            return HttpResponseServerError("Some server error occured")
    
    def put(request):
        body = json.loads(request.body)
        bookingId = body.get('bookingId', None)
        userId = body.get('user_id', None)
        hospitalId = body.get('hospital_id', None)
        bookingType = body.get('booking-type', None)
        bookingDate = body.get('booking_date', None)
        try:
            booking = Bookings.objects.filter(bookingId=bookingId).update(userId=userId, hospitalId=hospitalId, bookingType=bookingType, bookingDate=bookingDate)
            response = {
                'booking': booking
            }
            return JsonResponse(response)
        except Exception as e:
            return HttpResponseServerError("Some server error occured")
    
    def delete(self, request, *args, **kwargs):
        bookingId = kwargs.get('bookingId', None)
        try:
            Bookings.objects.filter(id=bookingId).delete()
            return HttpResponse('Booking deleted successsfully')
        except Exception as e:
            print(e)
            return HttpResponseServerError("Some server error occured")

class BookingType(View):

    def get(self, request, *args, **kwargs):
        try:
            types = BookingsType.objects.all()
            response = {
                'types': list(types.values())
            }
            return JsonResponse(response)
        except Exception as e:
            print(e)
            return HttpResponseServerError("Some server error occured")

    def post(self, request):
        body = json.loads(request.body)
        bookingType = body.get('bookingType', None)
        try:
            booking = BookingsType.objects.create(bookingType=bookingType)
            response = {
                'bookingTypeId': booking.id,
                'bookingType': booking.bookingType
            }
            return JsonResponse(response)
        except IntegrityError as ite:
            return HttpResponseForbidden("Booking Type already exists!")
        except Exception as e:
            print(e)
            return HttpResponseServerError("Some server error occured")
    
    def put(self, request):
        body = json.loads(request.body)
        bookingType = body.get('bookingType', None)
        try:
            booking = BookingsType.objects.filter(bookingType=bookingType).update(bookingType=bookingType)
            return HttpResponse('Booking type updated successfully.')
        except Exception as e:
            return HttpResponseServerError("Some server error occured")
    
    def delete(self, request, *args, **kwargs):
        body = json.loads(request.body)
        bookingType = body.get('bookingType', None)
        try:
            BookingsType.objects.filter(bookingType=bookingType).delete()
            return HttpResponse('Booking deleted successsfully')
        except Exception as e:
            print(e)
            return HttpResponseServerError("Some server error occured")

class UserBookings(View):

    def get(self, request, *args, **kwargs):
        userId = kwargs.get('userId', None)
        try:
            bookings = Bookings.objects.filter(userId=userId)
            response = {
                'bookings': list(bookings.values())
            }
            return JsonResponse(response)
        except Exception as e:
            print(e)
            return HttpResponseServerError("Some server error occured")

class Hospital(View):

    def get(self, request, *args, **kwargs):
        id = kwargs.get('id', None)
        try:
            if id == None:
                hospital = Hospitals.objects.all()
                response = {
                    'hospitals': list(hospital.values()),
                }
                return JsonResponse(response, content_type='application/json')
            else:
                hospital = Hospitals.objects.get(id=id)
                response = {
                    'hospital':{
                        'id': hospital.id,
                        'name': hospital.name,
                        'location': hospital.location,
                        'bedType': hospital.bedType,
                        'availability': hospital.availability,
                        'contact': hospital.contact
                    },
                }
                return JsonResponse(response, content_type='application/json')
        except Hospitals.DoesNotExist as e:
            return HttpResponse('Hospital details does not exist', status=401)
        except Exception as e:
            print(e)
            return HttpResponseServerError('Server Error Occured')
    
    def post(self, request):
        body = json.loads(request.body)
        name = body.get('name', None)
        bedType = body.get('bedType', None)
        availability = body.get('availability', None)
        location = body.get('location', None)
        contact = body.get('contact', None)
        try:
            hospital = Hospitals.objects.create(name=name, bedType=bedType, availability= availability, location= location, contact= contact)
            response = {
                'hospital':{
                    'id': hospital.id,
                    'name': hospital.name,
                    'location': hospital.location,
                },
            }
            return JsonResponse(response, content_type='application/json')
        except IntegrityError as ite:
            return HttpResponseForbidden("Hospital name already exists")
        except Exception as e:
            return HttpResponseServerError('Server Error Occured')
    
    def put(self, request):
        body = json.loads(request.body)
        name = body.get('name', None)
        bedType = body.get('bedType', None)
        availability = body.get('availability', None)
        location = body.get('location', None)
        contact = body.get('contact', None)
        try:
            hospital = Hospitals.objects.filter(name=name).update(bedType=bedType, availability= availability, location= location, contact= contact)
            response = {
                'message': 'Hospital details updated successfully' 
            }
            return JsonResponse(response, content_type='application/json')
        except IntegrityError as ite:
            return HttpResponseForbidden("Hospital name already exists")
        except Exception as e:
            return HttpResponseServerError('Server Error Occured')
    
    def delete(self, request):
        body = json.loads(request.body)
        name = body.get('name', None)
        try:
            hospital = Hospitals.objects.filter(name=name).delete()
            response = {
                'message': 'Hospital details deleted successfully' 
            }
            return JsonResponse(response, content_type='application/json')
        except IntegrityError as ite:
            return HttpResponseForbidden("Hospital name already exists")
        except Exception as e:
            print(e)
            return HttpResponseServerError('Server Error Occured')

def VaccineTypes(request):
    vaccineType = VaccineType.objects.all()
    vList = list(vaccineType.values())
    response = {}
    response['VaccineTypes'] = vList
    return JsonResponse(response, content_type='application/json')

def VaccineCentres(request):
    vaccineCentre = VaccineCentre.objects.all()
    vList = list(vaccineCentre.values())
    response = {}
    response['vaccineCentres'] = vList
    return JsonResponse(response, content_type='application/json')
