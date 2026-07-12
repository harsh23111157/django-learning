from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def home(request):
  return HttpResponse("shop home page")
# Create your views here.

def product(request):
  return HttpResponse("shop product  page")