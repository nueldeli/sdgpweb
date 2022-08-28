from django.shortcuts import render
from django.urls import reverse_lazy
from blog.models import Post
from django.views.generic import TemplateView

class HomeView(TemplateView):
	template_name = 'home.html'

	def get_context_data(self, **kwargs):
		context = super().get_context_data(**kwargs)
		context['latest_post'] = Post.objects.all()[:]
		return context

class AboutView(TemplateView):
	template_name = 'about.html'

class EventView(TemplateView):
	template_name = 'event.html'

class PublicationView(TemplateView):
	template_name = 'publication.html'