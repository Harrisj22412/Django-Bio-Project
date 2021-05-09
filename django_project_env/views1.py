#from django.shortcuts import render
from django.http  import HttpResponse

# Create your views here.

data = {
    'Name: Jalen Harris',
    ' City: Washington, DC'
    ' Course: Banckend, Python',
    " Message:"  "Coding is fun and challenging!"
}

def index_res(request):
    return HttpResponse(data)

