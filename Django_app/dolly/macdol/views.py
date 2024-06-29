from django.shortcuts import render
from django.http import HttpResponse


def michael(request):
    return render(request, 'dolly.html')
# Create your views here.
