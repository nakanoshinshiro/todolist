from django.shortcuts import render
from django.views.generic import ListView,DetailView,CreateView, DeleteView, UpdateView
from .models import TodoModel
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
# Create your views here.

class TodoList(LoginRequiredMixin,ListView):
    template_name = "list.html"
    model = TodoModel

class TodoDetail(LoginRequiredMixin,DetailView):
    template_name = "detail.html"
    model = TodoModel

class TodoCreate(LoginRequiredMixin,CreateView):
    template_name = "create.html"
    model = TodoModel
    fields = ("title","memo","priority","duedate")
    success_url = reverse_lazy("todo:list")

    def form_valid(self,form):
        todomodel = form.save(commit=False)
        todomodel.creator = self.request.user
        return super(TodoCreate,self).form_valid(form)


class TodoDelete(LoginRequiredMixin,DeleteView):
    template_name = "delete.html"
    model = TodoModel
    success_url = reverse_lazy("todo:list")


class TodoUpdate(LoginRequiredMixin,UpdateView):
    template_name = "update.html"
    model = TodoModel
    fields = ("title","memo","priority","duedate")
    success_url = reverse_lazy("todo:list")