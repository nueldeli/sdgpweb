from django.urls import path
from .views import ContactFormView, ContactSuccessView

urlpatterns = [
	path('add_message/', ContactFormView.as_view(), name='contact_form'),
	path('message_sent/', ContactSuccessView.as_view(), name='contact_success')
]