from django.http import HttpResponse
from django.shortcuts import render
from post.models import Post
# Create your views here.


def inicio(request):
    return render(request, "post/inicio.html")


def contacto(request):
    return render(request, "post/contacto.html")


def post_list(request):
    # ORM = Object-Relational Mapping / Mapeo Objecto-Relacional

    posts_tecnologia = (Post.objects.all()
        .order_by("-fecha_modificacion")
        .exclude(publicado=False)
    ) # SELECT * FROM post_post; / QuerySet([Post1, Post2, ...])
    try:
        posts_tecnologia = [Post.objects.get(id=10)]
    except (Post.DoesNotExist, Post.MultipleObjectsReturned):
        posts_tecnologia = []
    
    posts_tecnologia = (Post.objects
                        .filter(contenido__icontains="django", publicado=True)) # Si quiero ingnorar mayus/minus uso icontains. Sino contains
                        #.filter(contenido__istartswith="o"))
                        #.filter(contenido__endswith="django")) # Django, django, djangO, etc..
                        # __gt (Mayor que) / __gte (Mayor o igual que)
                        # __lt (Menor que) / __lte (Menor o igual que)
                        # autor_id__in=[2, 4, 10]
                        # autor__isnull=True / False
    if posts_tecnologia.exists() is True: # len(posts_tecnologia) mayor que 0  / posts_tecnologia.count() mayor que 0
        posts_tecnologia = posts_tecnologia[1]
    posts_tecnologia = Post.objects.all().first() # Me trae el PRIMER registro de la tabla
    posts_tecnologia = Post.objects.all().last() # Me trae el ULTIMO registro de la tabla
    cantidad_de_post = Post.objects.all().count()
    
    return render(request, "post/post_list.html", context={"posts_tecnologia": posts_tecnologia, "cantidad_post": cantidad_de_post})
