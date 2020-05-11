from django.shortcuts import render,redirect
from .models import *
from .forms import *

# Create your views here.


def index(request):
    tasks = task.objects.all()
    form = taskForms()
    if request.method == 'POST':
        form = taskForms(request.POST)
        if form.is_valid():
            form.save()
        return redirect('/')


    context = {'tasks': tasks,
                'form':form
               }
    return render(request, 'tasks/index.html', context)



def update(request,pk):
    taskes = task.objects.get(id=pk)

    form = taskForms(instance=taskes)
    if request.method == 'POST':
        form = taskForms(request.POST)
        if form.is_valid():
            form.save()
            return redirect(index)

    context = {'form':form}
    return render(request,'tasks/update.html',context)



def deletetask(request,pk):
    item = task.objects.get(id=pk)
    if request.method == 'POST':
        item.delete()
        return redirect(index)
  

    context = {'item':item}
    return render(request, 'tasks/delete.html',context)
