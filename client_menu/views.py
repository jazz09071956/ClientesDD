from django.shortcuts import render
from django.views import generic



class HomeView(generic.TemplateView):
    template_name = 'portada.html'
