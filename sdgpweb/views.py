from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import TemplateView

class HomeView(TemplateView):
	template_name = 'home.html'

class AboutView(TemplateView):
	template_name = 'about.html'

class EventView(TemplateView):
	template_name = 'event.html'