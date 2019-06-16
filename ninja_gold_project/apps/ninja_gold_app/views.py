from django.shortcuts import render, HttpResponse, redirect

# Create your views here.
def index(request):
    request.session['name'] = 'JOSH'

    # if request.POST['building'] == 'farm':
    #     request.session['name'] = 'FARM'

    # if request.method == "GET":
    #     print("a GET request is being made to this route")
    if request.method == "POST":
        print("a POST request is being made to this route")
        val_from_field_one = request.POST["one"]
        val_from_field_two = request.POST["two"]
        print(val_from_field_one)

    return render(request, "ninja_gold_app/index.html")
    #return HttpResponse("Hello Multiverse!")

def some_function(request):
    # request.session['name'] = request.POST['name']
    request.session['counter'] = 100