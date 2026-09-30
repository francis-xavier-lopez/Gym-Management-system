from django.shortcuts import render,HttpResponse

# Create your views here.
def display(request):
    return HttpResponse("Hello World")

def math(request):
    return HttpResponse("haii")