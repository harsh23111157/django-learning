from django.shortcuts import render
from datetime import datetime

# Create your views here.
class user:
  def __init__(self,name,age):
    self.name=name 
    self.age=age

def home(request):
  context={
    "name":"harshal patil",
    "age":"25",
    "skill":["python","django","react"],
    "user":user("harshal",21),
    "blog":{
      "title":"django template intro",
      "content":"<b>this is bold</b>",
      "author":{
        "name":"golu",
        "age":"dont know"
      },
      "created_at":datetime(2026,7,12,4,33),
    },
    "empty_value":None,

  }
  return render(request,"blog/home.html",context)