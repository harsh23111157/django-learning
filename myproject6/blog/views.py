from django.shortcuts import render
from datetime import datetime
# Create your views here.
def blog_details(request):
  post={
    "title":"My second template post",
    "description":"django is high level python web framework",
    "author":None,
    "created_at":datetime(2026,7,12,5,30),
    "comments_count":1,
    "tags":["django","python","react"],
    "price":100,
    "number":7,




  }
  return render(request,'blog/blog_details.html',{"post":post})
