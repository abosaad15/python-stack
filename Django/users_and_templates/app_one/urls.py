from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.run),
    path('add_user', views.add_user),
    path('show', views.show)
]
