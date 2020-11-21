from django.urls import path, include
from . import views
urlpatterns = [
    path('', views.login_registeration_page),
    path('register', views.register),
    path('login', views.login),
    path('trips', views.trips),
    path('logout', views.logout),

    path('trips/new', views.make_trip),
    path('add_trip', views.add_trip),

    path('remove_trip/<int:trip_id>', views.remove_trip),
    path('edit_trip/<int:trip_id>', views.edit_trip),

    path('update_trip/<int:trip_id>', views.update_trip),
    path('trips/<int:trip_id>', views.trip_info),

    path('join_trip/<int:trip_id>', views.join_trip),
    path('remove_joined_trip/<int:trip_id>', views.remove_joined_trip),
]
