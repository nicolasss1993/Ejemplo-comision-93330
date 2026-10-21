from django.urls import path
from django.views.generic import TemplateView

from post import views, views_cbv

urlpatterns = [
    path("", views.inicio, name="inicio"),
    path("contacto/", TemplateView.as_view(template_name="post/contacto.html"), name="contacto"),
    # path("post/list/", views.post_list, name="post_list"),
    # path("post/detail/<int:pk>", views.post_detail, name="post_detail"),
    # path("post/delete/<int:pk>", views.post_delete, name="post_delete"),
    # path("post/create/", views.post_create, name="post_create"),
    # path("post/update/<int:pk>", views.post_update, name="post_update"),
]

urlpatterns += [
    path("post/list/", views_cbv.PostListView.as_view(), name="post_list"),
    path("post/detail/<int:pk>", views_cbv.PostDetailView.as_view(), name="post_detail"),
    path("post/delete/<int:pk>", views_cbv.PostDeleteView.as_view(), name="post_delete"),
    path("post/create/", views_cbv.PostCreateView.as_view(), name="post_create"),
    path("post/update/<int:pk>", views_cbv.PostUpdateView.as_view(), name="post_update"),
]
