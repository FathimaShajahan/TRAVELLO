from django.shortcuts import render
from django.http import HttpResponse
from . models import Place


def index(request):
    obj=Place.objects.all()
    return render(request,'index.html',{'result':obj})