from django.urls import path

from post import views

urlpatterns = [
    path("", views.inicio, name="inicio"),
    path("contacto/", views.contacto, name="contacto"),
    path("post/list/", views.post_list, name="post_list"),
    path("post/detail/<int:pk>", views.post_detail, name="post_detail"),
    path("post/delete/<int:pk>", views.post_delete, name="post_delete"),
    path("post/create/", views.post_create, name="post_create"),
    path("post/update/<int:pk>", views.post_update, name="post_update"),
]
