from django.shortcuts import render, redirect, get_object_or_404

from .models import *
from .forms import *


# Create your views here.

# List todo_items
def index(request):
    template_name = "mTodo/index.html"
    todos = Todo.objects.all()
    context = {"todos": todos}
    return render(request, template_name, context)


# Adding new todo_item
def add_todo(request):
    template_name = "mTodo/new_todo.html"
    form = TodoForm()
    if request.method == 'POST':
        form = TodoForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect("index")
    context = {"form": form}
    return render(request, template_name, context)


# Editing todo_item
def update_todo(request, pk):
    todo = get_object_or_404(Todo, pk=pk)
    form = TodoForm(request.POST or None, instance=todo)
    if form.is_valid():
        form.save()
        return redirect("index")
    template_name = "mTodo/update_todo.html"
    return render(request, template_name, {"form": form})


# Deleting todo_item
def delete_todo(request, pk):
    todo = get_object_or_404(Todo, pk=pk)
    if request.method == 'POST':
        todo.delete()
        return redirect("index")
    template_name = "mTodo/delete_todo.html"
    return render(request, template_name, {"todo": todo})
