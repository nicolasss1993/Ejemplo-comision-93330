from django.contrib import admin
from post.models import Post


#admin.site.register(Post)


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    # Columnas visibles en la lista de registros
    list_display = ("autor", "titulo", "publicado")
    
    # Campo que funcionan como link para entrar a ver el registro
    list_display_links = ("autor", "titulo")
    
    # Habilita la barra de busqueda sobre estos campos
    search_fields = ("autor",)
    
    # Agrega el panel lateral de filtros para estos campos
    list_filter = ("fecha_creacion", "fecha_modificacion")
    
    # Orden por defecto de los registros en la lista
    ordering = ("autor", "titulo", "fecha_creacion")
    
    # Campo visible pero no editable en el formulario de admin
    readonly_fields = ("fecha_creacion", "codigo")
