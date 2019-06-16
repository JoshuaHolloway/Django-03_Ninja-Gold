from django.shortcuts import render, HttpResponse, redirect

# Create your views here.
def index(request):
    request.session['name'] = 'JOSH'

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
    print("You pressed a 'Find-Gold!' button")
    if request.POST['building'] == 'farm':
        request.session['name'] = 'YOU PRESSED FARM!'
        print("FARM")

    if request.POST['building'] == 'cave':
        request.session['name'] = 'YOU PRESSED CAVE!'
        print("FARM")

    if request.POST['building'] == 'house':
        request.session['name'] = 'YOU PRESSED HOUSE!'
        print("FARM")

    if request.POST['building'] == 'casino':
        request.session['name'] = 'YOU PRESSED CASINO!'
        print("FARM")

    # request.session['name'] = request.POST['name']
    request.session['counter'] = 100
    return render(request, "ninja_gold_app/index.html")
    #redirect("/")
    # return HttpResponse("Hello Multiverse!")