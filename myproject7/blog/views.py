from django.shortcuts import render
from datetime import datetime

def blog_list(request):
  blogs = [
    {"title":"django basics","is_featured":True,"author":"harshal"},
    {"title":"django advanced","is_featured":False,"author":""},
    {"title":"django rest framework","is_featured":False,"author":"harsh"},
    
  ]
  context={
    "blogs":blogs,
    "today":datetime.now(),
    "html_code":"<h1>welcome to my blog</h1>"

  }
  return render(request,'blog/blog_list.html',context)

# Create your views here.
