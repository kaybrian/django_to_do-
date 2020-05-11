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
    tasks = task.objects.get(id=pk)
    
    return render(request,'tasks/update.html')
