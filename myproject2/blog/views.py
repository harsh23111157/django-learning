from django.shortcuts import render
from django.http import HttpResponse

def post_details(request,post_id):
  return HttpResponse(f"<h1>show blog post{post_id}</h1>")

def user_profile(request,username):
  return HttpResponse(f"<h1>show username {username}</h1>")

def article_by_year(request,year):
  return HttpResponse(f"<h1>the year is : {year}</h1>")
# Create your views here.
# def article_details(request,year,month):
#   return HttpResponse(f"<h1>the year and month is : {year}-{month} </h1>")

def article_details(request,**kwargs):
  return HttpResponse(f"<h1>data:{kwargs}</h1>")