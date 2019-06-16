from django.shortcuts import render, HttpResponse, redirect
from random import randint
from datetime import datetime

# Create your views here.
def index(request):
    request.session['name'] = 'JOSH'

    if 'gold_sum' not in request.session:
        request.session['gold_sum'] = 0
    request.session['activities'] = []

    # if request.method == "GET":
    #     print("a GET request is being made to this route")
    if request.method == "POST":
        print("a POST request is being made to this route")
        val_from_field_one = request.POST["one"]
        val_from_field_two = request.POST["two"]
        print(val_from_field_one)
        print(val_from_field_two)
    return render(request, "ninja_gold_app/index.html")
# ============================================================
def process(request):
    building = request.POST['building']
    print(building) # DEBUG
    gold = 0
    if building == 'farm':
        gold = randint(10, 21)  # rand-num between 10-20
    if building == 'cave':
        gold = randint(5, 11)  # rand-num between 5-10
    if building == 'house':
        gold = randint(2, 6)  # rand-num between 2-5
    if building == 'casino':
        gold = randint(-100, 50)  # rand-num between -100:50

    # request.session['activities'].append({"result": result, "color": color})
    request.session['gold_sum'] += gold

    time = datetime.now()
    time = time.strftime("%Y/%m/%d %I:%M %p")
    result = ''
    if gold < 0:
        result = f'Lost {abs(gold)} golds from {building}, {time}'
        color = "text-danger"
    else:
        result = f'Earned {abs(gold)} golds from {building}, {time}'
        color = "text-success"

    request.session['activities'].append({"result": result, "color": color})

    # request.session['name'] = request.POST['name']
    request.session['counter'] = 100
    return render(request, "ninja_gold_app/index.html")
    #redirect("/")
    # return HttpResponse("Hello Multiverse!")