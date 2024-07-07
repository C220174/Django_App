from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def Hello(request):
    content = "<html><body><h1>Hello World</h1></body></html>"
    return HttpResponse(content)

def page(request):
    return render(request,'tmpl.html')
