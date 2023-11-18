from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import TodoForm
from .models import Todo

# Create your views here.

def index(request):
    todos = Todo.objects.order_by("-date")
    
    if request.method == "POST":
        form = TodoForm(request.POST)
        
        if form.is_valid():
            form.save()
            return redirect('index')
    form = TodoForm()
    
    page = {
        'forms': form,
        'list': todos,
        'title': 'Todo List'
    }
    
    return render(request, 'todo/index.html', page)

def remove(request, item_id):
    item = Todo.objects.get(id=item_id)
    item.delete()
    messages.info(request, f'Item "{item.title}" removed successfully!!!')
    return redirect('todo')