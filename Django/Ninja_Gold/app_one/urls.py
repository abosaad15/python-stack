from django.urls import path, include
from . import views
urlpatterns = [
    path('', views.run),
    path('process_money', views.process_money),
    path('delete_session', views.delete_session, name = 'reset')
]
