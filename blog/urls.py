from django.urls import path
from .views import PostIndexView

urlpatterns = [
	path('', PostIndexView.as_view(), name='post_index'),
]