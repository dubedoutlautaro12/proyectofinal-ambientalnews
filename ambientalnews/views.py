from django.shortcuts import render

from django.shortcuts import render
from django.views.generic import DetailView, ListView, CreateView, UpdateView, DeleteView, View
from ambientalnews.models import Post
from django.urls import reverse_lazy
from django.contrib.auth.views import LoginView, LogoutView
from ambientalnews.forms import UsuarioForm
from ambientalnews.models import Avatar, Post, Mensaje
from django.contrib.auth.admin import User
from django.contrib.auth.mixins import LoginRequiredMixin


def index(request):
    posts = Post.objects.order_by('-publicado_el').all()
    return render(request, "ambientalnews/index.html", {"posts": posts})


class PostDetalle(LoginRequiredMixin, DetailView):
    model = Post

class PostListar(ListView):
    model = Post  

class PostCrear(LoginRequiredMixin,CreateView):
    model = Post
    success_url = reverse_lazy("inicio")
    fields = '__all__'

class PostBorrar(LoginRequiredMixin, DeleteView):
    model = Post
    success_url = reverse_lazy("listar")

class PostActualizar(LoginRequiredMixin, UpdateView):
    model = Post
    success_url = reverse_lazy("listar")
    fields = "__all__"

class UserSignUp(CreateView):
    form_class = UsuarioForm
    template_name = 'registration/signup.html'
    success_url = reverse_lazy('inicio')


class UserLogin(LoginView):
    next_page = reverse_lazy('listar')

class UserLogout(LogoutView):
    next_page = reverse_lazy('inicio')

class AvatarActualizar(UpdateView):
    model = Avatar
    fields = ['imagen']
    success_url = reverse_lazy('inicio')


class UserActualizar(UpdateView):
    model = User
    fields = ['first_name', 'last_name', 'email']
    success_url = reverse_lazy('inicio')


class MensajeDetalle(LoginRequiredMixin, DetailView):
    model = Mensaje

class MensajeListar(LoginRequiredMixin, ListView):
    model = Mensaje  

class MensajeCrear(CreateView):
    model = Mensaje
    success_url = reverse_lazy("crear-mensaje")
    fields = ['nombre', 'email', 'texto']

class MensajeBorrar(LoginRequiredMixin, DeleteView):
    model = Mensaje
    success_url = reverse_lazy("listar-mensaje")


def Aboutme(request):
    return render (request, 'ambientalnews/about_me.html')