from django.shortcuts import render

def home(request):
  return render(request,'base.html')

def blog(request):
  student_list=[
    {"name":"mohit","class":"10th"},
    {"name":"harshal ","class":"9th"},
    {"name":"raj","class":"8th"},
  ]
   
  return render(request,'blog/blog.html',{"students":student_list})


# Create your views here.
