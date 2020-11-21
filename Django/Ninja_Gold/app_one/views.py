from django.shortcuts import render, HttpResponse, redirect
import random
from time import gmtime, strftime

# Create your views here.
def run(request):
    print("inside run")
    if 'gold_count' not in request.session:
        request.session['gold_count'] = 0
        request.session['activites'] = ''
        request.session['color'] = 1
    return render(request, 'index.html')


def process_money(request):
    print(request.POST)
    # print("gold before: ", request.session['gold_count'])
    # request.session['gold_count'] += int(request.POST['Gold'])
    # print("gold after: ", request.session['gold_count'])
    # print('inside process')
    # return render(request, 'index.html')
    print(request.POST)

    if request.POST['catagory'] == 'Farm':
        rand = random.randint(10,20)
        request.session['color'] = 1
        request.session['gold_count'] += rand
        # print("gold after: ", request.session['gold_count'])
        request.session['activites'] += "Earned " + str(rand) + " golds from the Farm! " + '(' +strftime("%Y-%m-%d %H:%M %p", gmtime()) +')' + "\n"
        print(request.session['activites'])
    elif request.POST['catagory'] == 'Cave':
        request.session['color'] = 1
        rand = random.randint(5,10)
        # print("gold after: ", request.session['gold_count'])
        request.session['activites'] += "Earned " + str(rand) + " golds from the Cave! " + '(' +strftime("%Y-%m-%d %H:%M %p", gmtime()) +')' + "\n"

        request.session['gold_count'] += rand
    elif request.POST['catagory'] == 'House':
        request.session['color'] = 1
        rand = random.randint(2,5)
        request.session['gold_count'] += rand
        # print("gold after: ", request.session['gold_count'])
        request.session['activites'] += "Earned " + str(rand) + " golds from the House! " + '(' +strftime("%Y-%m-%d %H:%M %p", gmtime()) +')' + "\n"

    elif request.POST['catagory'] == 'Casino':
        request.session['color'] = 1
        rand = random.randint(0,50)
        dest = random.randint(0,1)
        print(dest)

        if dest == 1:
            if request.session['gold_count'] - rand > -1 and rand > 0:
                request.session['gold_count'] -= rand
                request.session['color'] = 0
                request.session['activites'] += "Entered a casino and lost " + str(rand) + " ...Ouche... " + '(' +strftime("%Y-%m-%d %H:%M %p", gmtime()) +')' + "\n"

            else:
                request.session['gold_count'] = 0
                # request.session['color'] = 0
                request.session['activites'] += "You lost and your balance is reseted to Zero " + '(' +strftime("%Y-%m-%d %H:%M %p", gmtime()) +')' + "\n"

        else:
            request.session['gold_count'] += rand
            request.session['color'] = 1
            request.session['activites'] += "Earned " + str(rand) + " golds from the Casino! " + '(' +strftime("%Y-%m-%d %H:%M %p", gmtime()) +')' + "\n"

    return redirect('/')



def delete_session(request):
    del request.session['gold_count']
    del request.session['activites']
    return redirect('/')

