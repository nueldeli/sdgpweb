from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import Post
from .forms import AddPostForm, UpdatePostForm

# Create your views here.
class PostIndexView(ListView):
	model = Post
	template_name = 'blog/post_index.html'

class PostDetailView(DetailView):
	model = Post
	template_name = 'blog/post_detail.html'

class PostAddView(CreateView):
	model = Post
	form_class = AddPostForm
	template_name = 'blog/post_add.html'

class PostUpdateView(UpdateView):
	model = Post
	form_class = UpdatePostForm
	template_name = 'blog/post_update.html'

class PostDeleteView(DeleteView):
	model = Post
	template_name = 'blog/post_delete.html'