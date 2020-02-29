from django.shortcuts import render, redirect
from .models import Task
from .forms import TaskForm
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage # for paginatation
from todo import helpers
from django.http import HttpResponseNotFound

def home(request):
    
    if request.method == "POST":
        form = TaskForm(request.POST)

        if form.is_valid():
            taskObject = Task(note=form.cleaned_data['note'])
            taskObject.save()
            return redirect('todo-home')

    else:
        form = TaskForm()
        tasks = Task.objects.order_by("-created_on").all()
        # per page 7 records data will be displayed 
        tasks = helpers.page_records(request, tasks, 7)
        
        context = {
            'form':form,
            'tasks': tasks
            }  

    return render(request, 'todoApp/home.html', context)


def about(request):
    return render(request, 'todoApp/about.html')   


def delete(request, pk):
    try:
        task = Task.objects.get(pk = pk)
        task.delete()
        return redirect('todo-home')      
    except Task.DoesNotExist:
       return HttpResponseNotFound('<h2> Sorry! Page  is not found </h2>')
   

def update(request, pk):
    form= TaskForm()
    
    if request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            task = Task.objects.filter(pk = pk).update(note = form.cleaned_data['note'])
            print(task)
            return redirect('todo-home')

    
    return render(request, 'todoApp/update.html', {'form': form})

# in future, I will add more functionality for an exmaple - Django authentication
# User logging in and out and profile dashboard
def login(request):
    return render(request, 'todoApp/login.html')

def register(request):
    return render(request, 'todoApp/register.html')



