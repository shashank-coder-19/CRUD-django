from django.shortcuts import render
from django.views.generic import View, TemplateView, ListView, DetailView, CreateView, UpdateView, DeleteView
from  . import models
from django.urls import reverse_lazy

# Create your views here.
class IndexView(TemplateView):
    template_name='index.html'




class SchoolLIstView(ListView):
    context_object_name='schools'
    # it redefines context dictionary name to be schools
    model=models.School
    # it returns a context dictionary with name school_list , it lowercase your model name and add list to it


class SchoolDetailView(DetailView):
    context_object_name='school_detail'
    model=models.School
    template_name='basic_app/school_detail.html'


class SchoolCreateView(CreateView):
    fields=('name','location','principal')
    model=models.School

    # createview and UpdateView takes care of making forms as well so we do not have to worry about making forms independently

class SchoolUpdateView(UpdateView):
    fields=('name','principal')
    model=models.School

class SchoolDeleteView(DeleteView):
    model=models.School
    success_url=reverse_lazy('basic_app:list')
