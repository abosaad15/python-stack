from django.shortcuts import render, redirect
from .models import Book, Author
# Create your views here.


def add_book(request):
    Book.objects.create(title = request.POST['title'], desc = request.POST['desc'])
    return redirect('/')

def books(request):
    context = {
        'books' : Book.objects.all()
    }
    return render(request, 'add_book.html', context)


def book_info(request, id):
    book = Book.objects.get(id = id)
    authors = Author.objects.all()
    context = {
        'authors' : authors,
        'book' : book
    }
    return render(request, 'book_info.html', context)

def link_author(request, book_id):
    book = Book.objects.get(id = book_id)
    author_id = request.POST['author_id']
    author = Author.objects.get(id = author_id)
    book.authors.add(author_id)
    book.save()
    # print(author.books.all())

    return redirect('/')

#----------------------------------------

def add_author(request):
    Author.objects.create(first_name = request.POST['first_name'], last_name = request.POST['last_name'], notes = request.POST['notes'])
    return redirect('/authors')

def authors(request):
    context = {
        'authors' : Author.objects.all()
    }
    return render(request, 'add_author.html', context)


def author_info(request, id):
    author = Author.objects.get(id = id)
    books = Book.objects.all()
    context = {
        'author' : author,
        'books' : books,
    }
    print(context['books'])
    return render(request, 'author_info.html', context)



def link_book(request, author_id):
    author = Author.objects.get(id = author_id)
    book_id = request.POST['book_id']
    book = Book.objects.get(id = book_id)
    author.books.add(book_id)
    author.save()
    # print(author.books.all())

    return redirect('/authors')
