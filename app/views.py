from django.shortcuts import render, HttpResponse

# Create your views here.

def home(request):
    # return HttpResponse("Hello World")
    return render(request, "home.html")

def about(request):
    # return HttpResponse("This is the about page")
    return render(request, "about.html")

def contact(request):
    return HttpResponse("This is the contact page")



