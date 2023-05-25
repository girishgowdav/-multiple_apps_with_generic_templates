from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
def one(request):
    return HttpResponse('hai')
def pageone(request):
    return render(request,'pageone.html')