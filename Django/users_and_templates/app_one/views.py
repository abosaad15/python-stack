from django.shortcuts import render, redirect
from .models import User
# Create your views here.

def run(request):
    # objs = User.objects.all()
    # for i in objs:
    #     i.delete()

    # print(User.objects.all())
    return render(request, 'index.html')


def add_user(request):

    user = User.objects.create(first_name= request.POST['first_name'], last_name= request.POST['last_name'], email= request.POST['email'], age= request.POST['age'])
    # context = {
    #     'users' : User.objects.all()
    # }

    # request.session['first_name'] = request.POST['first_name']
    # request.session['last_name'] = request.POST['last_name']
    # request.session['email'] = request.POST['email']
    # request.session['users'] = request.POST['age']

    # return render(request,'table.html', context)
    return redirect('/show')



def show(request):
    context = {
        'users' : User.objects.all()
    }
    return render(request,'table.html', context)
