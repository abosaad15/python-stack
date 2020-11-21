from django.shortcuts import render, redirect
from .models import Dojo, Ninja
# Create your views here.
def run(request):
    context = {
        'dojos' : Dojo.objects.all(),
        'ninjas' : Ninja.objects.all()
    }
    return render(request, 'index.html', context)



def add_dojo(request):
    dojo = Dojo.objects.create(name = request.POST['name'], city = request.POST['city'], state = request.POST['state'])
    print(dojo.name)
    return redirect('/show')



def add_ninja(request):
    dojo_id = int(request.POST['dojo'])
    ninja = Ninja.objects.create(first_name = request.POST['first_name'], last_name = request.POST['last_name'], dojo_id = Dojo.objects.get(id = dojo_id))
    print(type(request.POST['dojo']))
    return redirect('/show')


def show(request):
    context = {
        'dojos' : Dojo.objects.all(),
        'ninjas' : Ninja.objects.all()
    }

    return render(request, 'show.html', context)
