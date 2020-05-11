from django.shortcuts import render
from .models import *
from .forms import *

# Create your views here.


def index(request):
    tasks = task.objects.all()
    form = taskForms()

    context = {'tasks': tasks,
                'form':form
               }
    return render(request, 'tasks/index.html', context)
