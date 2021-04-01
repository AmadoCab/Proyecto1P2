from django.shortcuts import render, get_object_or_404
from django.contrib.auth.models import User
from .models import Project
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.views.generic import (
    ListView,
    DetailView,
    CreateView,
    UpdateView,
    DeleteView
)

def home(request):
    return render(request,'mdtranslate/home.html')

class UserProjectsView(LoginRequiredMixin, ListView):
    model = Project
    template_name = 'mdtranslate/projects.html'
    context_object_name = 'prjs'

    def get_queryset(self):
        user = self.request.user
        #user = get_object_or_404(User, username=self.kwargs.get('username'))
        return Project.objects.filter(author=user).order_by('-date_modified')

class ProjectDetailView(DetailView): # «<app>/<model>_<viewtype>.html»
    model = Project
    context_object_name = 'prj'

class ProjectCreateView(LoginRequiredMixin, CreateView):
    model = Project
    fields = ['title', 'content']

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

class ProjectUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Project
    fields = ['title', 'content']

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        return False

class ProjectDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Project
    success_url = '/projects/'

    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        return False
