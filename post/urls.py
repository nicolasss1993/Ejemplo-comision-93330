from django.urls import path

from post import views

urlpatterns = [
    path("", views.inicio, name="inicio"),
    path("post/list/", views.post_list, name="post_list"),
]
