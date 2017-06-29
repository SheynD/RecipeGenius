from django.shortcuts import render
from django.contrib import messages
from django.core.urlresolvers import reverse
from django.shortcuts import redirect, get_object_or_404
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from models import *
from forms import *

# Create your views here.
class PostListView(ListView):
    model = Post
    context_object_name = "post_list"

    def get_template_names(self):
        return ["foodnetworkapp/list.html"]

    def get_queryset(self):
        posts = Post.objects
        if 'all_posts' not in self.request.GET:
            posts = posts.filter(is_published=True)
        return posts

class PostCreateView(CreateView):
    model = Post
    form_class = PostForm

    def get_template_names(self):
        return ["foodnetworkapp/create.html"]

    def get_success_url(self):
        return reverse('list')
  
    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.user = self.request.user
        messages.success(self.request, "The post has been created.")
        return super(PostCreateView, self).form_valid(form)

class PostDetailView(DetailView):
    model = Post
    context_object_name = "post"

    def get_template_names(self):
        return ["foodnetworkapp/detail.html"]

    def get_object(self):
        return Post.objects(id=self.kwargs['pk'])[0]

class PostUpdateView(UpdateView):
    model = Post
    form_class = PostForm
    context_object_name = "post"

    def get_template_names(self):
        return ["foodnetworkapp/update.html"]

    def get_success_url(self):
      return reverse('list')

    def form_valid(self, form):
        self.object = form.save()
        messages.success(self.request, "The post has been updated.")
        return super(PostUpdateView, self).form_valid(form)

    def get_object(self):
        return Post.objects(id=self.kwargs['pk'])[0]

class PostDeleteView(DeleteView):
    model = Post

    def get_success_url(self):
        return reverse('list')

    def get(self, *args, **kwargs):
        """ Skip confirmation page """
        return self.delete(self.request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        self.object = self.get_object()
        self.object.delete()
        messages.success(self.request, "The post has been removed.")
        return redirect(self.get_success_url())

    def get_object(self):
        return Post.objects(id=self.kwargs['pk'])[0]
