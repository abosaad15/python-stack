from django.urls import path, include
from . import views
urlpatterns = [
    path('', views.books),
    path('authors', views.authors),
    path('add_author', views.add_author),
    path('add_book', views.add_book),
    path('authors/<int:id>', views.author_info),
    path('books/<int:id>', views.book_info),
    path('link_book/<int:author_id>', views.link_book),
    path('link_author/<int:book_id>', views.link_author),
]
