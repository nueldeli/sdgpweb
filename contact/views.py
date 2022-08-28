from django.shortcuts import render
from .models import Contact
from .forms import AddMessageForm
from django.views.generic import TemplateView, CreateView

# Create your views here.
class ContactFormView(CreateView):
	model = Contact
	form_class = AddMessageForm
	template_name = 'contact/contact_form.html'

class ContactSuccessView(TemplateView):
	template_name = 'contact/contact_success.html'