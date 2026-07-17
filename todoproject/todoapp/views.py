from django.shortcuts import render,redirect,get_object_or_404
from .models import Task
from django.urls import reverse

# Create your views here.
def task_list(request):
  task=Task.objects.all().order_by('-created_at')
  return render(request,'todoapp/task_list.html',{'tasks':task})

def task_create(request):
  if request.method == 'POST':
    title=request.POST.get('title','').strip()
    description=request.POST.get('description','').strip()
    if title:
      Task.objects.create(title=title,description=description)
      return redirect(reverse('todoapp:task_list'))
    error='title cannot be empty'
    return render(request,'todoapp/task_form.html',{'error':error})
  return render(request,'todoapp/task_form.html')  

def task_update(request,pk):
  task=get_object_or_404(Task,pk=pk)
  if request.method =='POST':
    title=request.POST.get('title','').strip()
    description=request.POST.get('description','').strip()
    completed=request.POST.get('completed')=='on'
    if title:
      task.title=title
      task.description=description
      task.completed=completed
      task.save()
      return redirect(reverse('todoapp:task_list'))
    return render(request,'todoapp/task_form.html',{'task':task,'error':'Title cant be empty'})
  return render(request,'todoapp/task_form.html',{'task':task})

def task_delete(request,pk):
  task=get_object_or_404(Task,pk=pk)
  if request.method=='POST':
    task.delete()
    return redirect(reverse('todoapp:task_list'))
  return render(request,'todoapp/task_confirm_delete.html',{'task':task})

def task_toggle_complete(request,pk):
  task=get_object_or_404(Task,pk=pk)
  if request.method=='POST':
    task.completed= not task.completed
    task.save()
  return redirect('todoapp:task_list')  



