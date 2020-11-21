from django.shortcuts import render, HttpResponse, redirect
import bcrypt
from django.contrib import messages
from time import gmtime, strftime
# Create your views here.


from .models import Trip, User
from django.contrib import messages


#------------------------------------------------

def trip_info(request, trip_id):
    context = {
        'trip' : Trip.objects.get(id = trip_id),
        'user' : User.objects.get(id = request.session['userid']),
    }
    return render(request, 'trip_info.html', context)


#------------------------------------------------

def join_trip(request, trip_id):
     trip = Trip.objects.get(id = trip_id)
     user = User.objects.get(id = request.session['userid'])
     user.joined_trips.add(trip)
     return redirect(trips)


#------------------------------------------------

def remove_joined_trip(request, trip_id):
     trip = Trip.objects.get(id = trip_id)
     user = User.objects.get(id = request.session['userid'])
     user.joined_trips.remove(trip)
     return redirect(trips)


#------------------------------------------------

def login_registeration_page(request):
    return render(request, 'index.html')


#-----------------------------------------------


def trips(request):
    context = {
        'trips' : User.objects.get(id = request.session['userid']).trips.all(),
        'joined_trips' : User.objects.get(id = request.session['userid']).joined_trips.all(),
        'user' : User.objects.get(id = request.session['userid']),

        'all_users' : User.objects.all(),
    }
    return render(request, 'dashboard.html', context)

#-----------------------------------------------

def make_trip(request):
    context = {
        'user' : User.objects.get(id = request.session['userid'])
    }

    return render(request, 'make_trip.html', context)

#-----------------------------------------------

def edit_trip(request, trip_id):
    context = {
        'trip' : Trip.objects.get(id = trip_id),
        'user' : User.objects.get(id = request.session['userid']),
    }
    return render(request, 'edit_trip.html', context)

#-----------------------------------------------

def logout(request):
    del request.session['userid']
    return redirect(login_registeration_page)

#-----------------------------------------------


#-----------------------------------------------

def remove_trip(request, trip_id):
    trip = Trip.objects.get(id = trip_id)
    trip.delete()
    # User.objects.get(id = request.session['userid']).wishes.remove(wish)
    return redirect(trips)

#-----------------------------------------------

def update_trip(request, trip_id):
    errors = Trip.objects.basic_validator(request.POST)
    if len(errors) > 0:
        for key, value in errors.items():
            messages.error(request, value)
        errors = {}
        return redirect(edit_trip, trip_id)
    else:
        trip = Trip.objects.get(id = trip_id)
        trip.dest = request.POST['dest']
        trip.start_date = request.POST['start_date']
        trip.end_date = request.POST['end_date']
        trip.plan = request.POST['plan']
        trip.save()
        return redirect(trips)

#-----------------------------------------------

def add_trip(request):
    errors = Trip.objects.basic_validator(request.POST)
    if len(errors) > 0:
        for key, value in errors.items():
            messages.error(request, value)
        errors = {}
        return redirect(make_trip)
    else:
        user = User.objects.get(id = request.session['userid'])
        trip = Trip.objects.create(dest = request.POST['dest'], plan = request.POST['plan'], user = user, start_date = request.POST['start_date'], end_date = request.POST['end_date'])
        # user.trips.add(trip)
        return redirect(trips)

#-----------------------------------------------

def register(request):
    errors = User.objects.basic_validator(request.POST)
    if len(errors) > 0:
        for key, value in errors.items():
            messages.error(request, value)
        return redirect(login_registeration_page)
    else:
        if request.POST['password'] == request.POST['pw_conf']:
            password = request.POST['password']
            pw_hash = bcrypt.hashpw(password.encode(), bcrypt.gensalt()).decode()
            print(pw_hash)

            User.objects.create(first_name = request.POST['first_name'], last_name = request.POST['last_name'], email = request.POST['email'], password = pw_hash)

            state = 'Registeration is successful'
            return redirect(login_registeration_page)
        else:
            messages.error(request, "Password did not match")
            return redirect(login_registeration_page)

#-----------------------------------------------

def login(request):
    user = User.objects.filter(email=request.POST['email'])
    if user:
        logged_user = user[0]
        if bcrypt.checkpw(request.POST['password'].encode(), logged_user.password.encode()):
            request.session['userid'] = logged_user.id
            return redirect(trips)
        else:
            messages.error(request, 'your Password is not correct')
    else:
        messages.error(request, 'your Email is not registered')

    return redirect(login_registeration_page)
