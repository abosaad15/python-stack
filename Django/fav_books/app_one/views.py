from django.shortcuts import render, HttpResponse, redirect
import bcrypt
from django.contrib import messages

# Create your views here.
from .models import Book, User
from django.contrib import messages

def login_registeration_page(request):
    return render(request, 'index.html')

#------------------------------------------------

def logout(request):
    del request.session['userid']
    return redirect('/')

#------------------------------------------------

def book_info(request, book_id):
    context = {
        'user' : User.objects.get(id=request.session['userid']),
        'book' : Book.objects.get(id = book_id)
    }
    return render(request, 'book_info.html', context)

#------------------------------------------------

def delete(request, book_id):
    book = Book.objects.get(id = book_id)
    book.delete()
    return redirect('/books')

#------------------------------------------------

def update(request, book_id):
    book = Book.objects.get(id = book_id)
    book.desc = request.POST['desc']
    book.save()
    return redirect('/books')

#-----------------------------------------------

def books(request):
    context = {
        'user' : User.objects.get(id=request.session['userid']),
        'books' : Book.objects.all(),
        # 'favBooks' : User.objects.get(id=request.session['userid']).liked_books.all(),
    }
    return render(request, 'books.html', context)

#-----------------------------------------------

def add_book(request):
    errors = Book.objects.basic_validator(request.POST)
    if len(errors) > 0:
        for key, value in errors.items():
            messages.error(request, value)
        return redirect('/books')

    user = User.objects.get(id = request.session['userid'])
    book = Book.objects.create(title = request.POST['title'], desc = request.POST['desc'], uploaded_by = user)
    user.liked_books.add(book)
    return redirect(books)

#-----------------------------------------------

def add_to_fav_list(request, book_id):
    user = User.objects.get(id=request.session['userid'])
    user.liked_books.add(Book.objects.get(id = book_id))

    return redirect(book_info, book_id = book_id)

#-----------------------------------------------

def unfavorite(request, book_id):
    user = User.objects.get(id=request.session['userid'])
    user.liked_books.remove(Book.objects.get(id = book_id))

    return redirect(book_info, book_id = book_id)

#-----------------------------------------------

def register(request):
    errors = User.objects.basic_validator(request.POST)
    if len(errors) > 0:
        for key, value in errors.items():
            messages.error(request, value)
        return redirect('/')
    else:
        if request.POST['password'] == request.POST['pw_conf']:
            password = request.POST['password']
            pw_hash = bcrypt.hashpw(password.encode(), bcrypt.gensalt()).decode()
            print(pw_hash)

            User.objects.create(first_name = request.POST['first_name'], last_name = request.POST['last_name'], email = request.POST['email'], password = pw_hash)

            state = 'Registeration is successful'
            return redirect('/')
        else:
            messages.error(request, "Password did not match")
            return redirect('/')

#-----------------------------------------------

def login(request):
    user = User.objects.filter(email=request.POST['email'])
    if user:
        logged_user = user[0]
        if bcrypt.checkpw(request.POST['password'].encode(), logged_user.password.encode()):
            request.session['userid'] = logged_user.id
            return redirect('/books')
        else:
            messages.error(request, 'your Password is not correct')
    else:
        messages.error(request, 'your Email is not registered')

    return redirect('/')
