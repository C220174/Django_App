from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def Bye(request):
    content = "<html><body><h1>Hi Bye!</h1></body></html>"
    return HttpResponse(content)
