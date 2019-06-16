from django.shortcuts import render, HttpResponse, redirect
from random import randint

# Create your views here.
def index(request):
    request.session['name'] = 'JOSH'
    request.session['gold_sum'] = 0

    # if request.method == "GET":
    #     print("a GET request is being made to this route")
    if request.method == "POST":
        print("a POST request is being made to this route")
        val_from_field_one = request.POST["one"]
        val_from_field_two = request.POST["two"]
        print(val_from_field_one)
        print(val_from_field_two)

    return render(request, "ninja_gold_app/index.html")


def process(request):

    # Initialize stuff
    gold = 0
    building = ""

    if request.POST['building'] == 'farm':
        print("FARM")  # DEBUG
        request.session['name'] = 'YOU PRESSED FARM!'
        gold = randint(10,21) #rand-num between 10-20
        building = 'farm'

    if request.POST['building'] == 'cave':
        print("CAVE")  # DEBUG
        request.session['name'] = 'YOU PRESSED CAVE!'
        gold = randint(5,11) #rand-num between 5-10
        building = 'cave'

    if request.POST['building'] == 'house':
        print("HOUSE")  # DEBUG
        request.session['name'] = 'YOU PRESSED HOUSE!'
        gold = randint(2,6) #rand-num between 2-5
        building = 'house'

    if request.POST['building'] == 'casino':
        print("CASINO")  # DEBUG
        request.session['name'] = 'YOU PRESSED CASINO!'
        gold = randint(-100,50) #rand-num between -100:50
        building = 'casino'


    # request.session['activities'].append({"result": result, "color": color})
    request.session['gold_sum'] += gold


    # request.session['name'] = request.POST['name']
    request.session['counter'] = 100
    return render(request, "ninja_gold_app/index.html")
    #redirect("/")
    # return HttpResponse("Hello Multiverse!")