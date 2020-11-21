from django.urls import path, include
from . import views


urlpatterns = [
    path('', views.index),
    path('addCourse', views.addCourse),
    path('courses/destroy/<int:course_id>', views.destroy),
    path('delete/<int:course_id>', views.delete),
]
