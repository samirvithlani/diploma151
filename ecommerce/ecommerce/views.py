from django.http import HttpResponse
from django.shortcuts import render

greet = "Hello World"
def index(request):
    return HttpResponse(greet)

def aboutus(request):
    return HttpResponse("About Us")

def contactUs(request):
    return render(request,'contactus.html')

def blog(request):
    return render(request,'blogs/blog.html')