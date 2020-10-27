from django.shortcuts import render
from django.http import HttpResponse
from . models import Test
def index(request):
    return render(request,'index.html')
def abc(request):
    res=Test.objects.all()
    return render(request,'index.html',{'result':res})


# Create your views here.
