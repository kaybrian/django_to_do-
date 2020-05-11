from django.shortcuts import render
from .models import * 
# Create your views here.
def index(request):
    tasks = task.objects.all()
    context 
    return render(request,'tasks/index.html')