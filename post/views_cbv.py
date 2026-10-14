from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.urls import reverse_lazy
from django.views.generic import DetailView, ListView, TemplateView
from django.views.generic.edit import CreateView, DeleteView, UpdateView

from post.forms import PostForm
from post.models import Post


# --- Vistas simples, sin modelo -------------------------------------------

class InicioView(TemplateView):
    template_name = "post/inicio.html"


class ContactoView(TemplateView):
    # Equivale a:
    #   def contacto(request):
    #       return render(request, "post/contacto.html")
    template_name = "post/contacto.html"


# --- Listado y detalle (solo lectura) --------------------------------------

class PostListView(ListView):
    model = Post
    template_name = "post/post_list.html"
    context_object_name = "post_tecnologia"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["cantidad_post"] = Post.objects.all().count()
        return context


class PostDetailView(DetailView):
    # Equivale a:
    #   def post_detail(request, pk):
    #       post = Post.objects.get(id=pk)
    #       return render(request, "post/post_detail.html", {"post": post})
    model = Post
    template_name = "post/post_detail.html"
    context_object_name = "post"  # por defecto sería "object"


# --- Crear, editar y borrar (requieren login + ser el autor) --------------

class PostCreateView(LoginRequiredMixin, CreateView):
    # Equivale a:
    #   @login_required
    #   def post_create(request):
    #       if request.method == "POST":
    #           form = PostForm(request.POST, request.FILES)
    #           if form.is_valid():
    #               post = form.save(commit=False)
    #               post.autor = request.user
    #               post.save()
    #               return redirect("post_list")
    #       form = PostForm()
    #       return render(request, "post/post_form.html", {"form": form})
    model = Post
    form_class = PostForm
    template_name = "post/post_form.html"
    success_url = reverse_lazy("post_list")

    def form_valid(self, form):
        # form_valid se ejecuta solo cuando el formulario ya es válido.
        # Es el lugar equivalente a "post.save(commit=False)" + asignar
        # el autor antes de guardar.
        form.instance.autor = self.request.user
        return super().form_valid(form)


class PostUpdateView(LoginRequiredMixin, UpdateView):
    # Equivale a:
    #   @login_required
    #   def post_update(request, pk):
    #       post = Post.objects.get(id=pk)
    #       if post.autor != request.user:
    #           return HttpResponseForbidden("No tenés permiso para editar este post.")
    #       if request.method == "POST":
    #           form = PostForm(request.POST, request.FILES, instance=post)
    #           if form.is_valid():
    #               form.save()
    #               return redirect("post_list")
    #       form = PostForm(instance=post)
    #       return render(request, "post/post_form.html", {"form": form})
    model = Post
    form_class = PostForm
    template_name = "post/post_form.html"
    success_url = reverse_lazy("post_list")



class PostDeleteView(LoginRequiredMixin, DeleteView):
    model = Post
    template_name = "post/post_confirm_delete.html"
    context_object_name = "post"
    success_url = reverse_lazy("post_list")
