from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User

# Create your models here.
class Contact(models.Model):
	date_written = models.DateTimeField(auto_now_add=True)
	author = models.CharField(max_length=100, null=True)
	email = models.CharField(max_length=200, null=True)
	message = models.TextField()

	class Meta:
		ordering = ['-date_written']

	def __str__(self):
		return self.date_written + ' | ' + str(self.author)

	def get_absolute_url(self):
		return reverse('contact_success')
