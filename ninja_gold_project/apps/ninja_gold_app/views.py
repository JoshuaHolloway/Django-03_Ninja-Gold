from django.shortcuts import render, HttpResponse

# Create your views here.
def index(request):
    return render(request, "ninja_gold_app/index.html")
    #return HttpResponse("Hello Multiverse!")