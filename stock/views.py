from django.shortcuts import get_object_or_404,render
from django.http import HttpResponseRedirect,HttpResponse
from django.urls import reverse

# Create your views here.

def index(request):
    return render(request,'stock/index.html')