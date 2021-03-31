from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.

def home(request):

    return HttpResponse("Hello, This is Sanket from T3 Batch and my PRN is 1841043.")
