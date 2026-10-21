from typing import Any

from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.contrib.messages.views import SuccessMessageMixin
from django.db.models.query import QuerySet
from django.urls import reverse_lazy
from django.views.generic import DetailView, ListView, TemplateView
from django.views.generic.edit import CreateView, DeleteView, UpdateView

from post.forms import PostForm
from post.models import Post

# --- Vistas simples, sin modelo -------------------------------------------


# class InicioView(TemplateView):
#     template_name = "post/inicio.html"


# class ContactoView(TemplateView):
#     # Equivale a:
#     #   def contacto(request):
#     #       return render(request, "post/contacto.html")
#     template_name = "post/contacto.html"


# --- Listado y detalle (solo lectura) --------------------------------------


class PostListView(ListView):
    model = Post
    # template_name = "post/post_list.html"
    context_object_name = "post_tecnologia"  # predeterminado: object_list

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["cantidad_post"] = Post.objects.all().count()
        return context

    def get_queryset(self) -> QuerySet:
        busqueda = self.request.GET.get("busqueda")
        if busqueda:
            posts = Post.objects.filter(titulo__icontains=busqueda)
        else:
            posts = Post.objects.all()
        return posts


class PostDetailView(DetailView):
    model = Post
    # template_name = "post/post_detail.html"
    context_object_name = "post"  # por defecto sería "object"


# --- Crear, editar y borrar (requieren login + ser el autor) --------------


class PostCreateView(LoginRequiredMixin, SuccessMessageMixin, CreateView):
    model = Post
    form_class = PostForm
    # template_name = "post/post_form.html"
    success_url = reverse_lazy("post_list")
    success_message = "El post fue creado exitosamente"

    def form_valid(self, form):
        # form_valid se ejecuta solo cuando el formulario ya es válido.
        # Es el lugar equivalente a "post.save(commit=False)" + asignar
        # el autor antes de guardar.
        form.instance.autor = self.request.user
        return super().form_valid(form)


class PostUpdateView(LoginRequiredMixin, SuccessMessageMixin, UpdateView):
    model = Post
    form_class = PostForm
    # template_name = "post/post_form.html"
    success_url = reverse_lazy("post_list")
    success_message = "El post fue editado exitosamente"


class PostDeleteView(LoginRequiredMixin, SuccessMessageMixin, DeleteView):
    model = Post
    template_name = "post/post_confirm_delete.html"
    context_object_name = "post"
    success_url = reverse_lazy("post_list")
    success_message = "El post fue eliminado"
