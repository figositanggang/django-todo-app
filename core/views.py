from django.shortcuts import render
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy

from .models import Todo


class TodoList(ListView):
    model = Todo


class TodoView(DetailView):
    model = Todo


class CreateTodo(CreateView):
    model = Todo
    fields = ["name"]
    success_url = reverse_lazy("todo_list")


class UpdateTodo(UpdateView):
    model = Todo
    fields = ["name"]
    success_url = reverse_lazy("todo_list")


class DeleteTodo(DeleteView):
    model = Todo
    success_url = reverse_lazy("todo_list")
