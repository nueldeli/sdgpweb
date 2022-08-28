from django import forms
from .models import Contact
from django.utils.translation import gettext_lazy as _

class AddMessageForm(forms.ModelForm):
	class Meta:
		model = Contact
		fields = ('author', 'email', 'message')

		widgets ={
			'author':forms.TextInput(attrs={'class':'form-control', 'placeholder':'Full name'}),
			'email':forms.TextInput(attrs={'class':'form-control', 'placeholder':'Email'}),
			'message':forms.Textarea(attrs={'class':'form-control', 'placeholder':'Enter your message here'})
		}

		labels = {
			'author':_(''),
			'email':_(''),
			'message':_(''),
		}
