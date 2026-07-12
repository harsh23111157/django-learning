from django.shortcuts import render
from django.http import HttpResponse


def home(request):
  return HttpResponse("blog home page")
# Create your views here.

def about(request):
  return HttpResponse("blog about page")