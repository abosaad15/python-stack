
from django.urls import path, include
from . import views
urlpatterns = [
    path('', views.login_registeration_page),
    path('register', views.register),
    path('login', views.login),
    path('logout', views.logout),
    path('books', views.books),
    path('add_book', views.add_book),
    path('add_to_fav_list/<int:book_id>', views.add_to_fav_list),
    path('book_info/<int:book_id>', views.book_info),
    path('update/<int:book_id>', views.update),
    path('delete/<int:book_id>', views.delete),
    path('unfavorite/<int:book_id>', views.unfavorite),

]
