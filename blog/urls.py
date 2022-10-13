from xml.etree.ElementInclude import include
from django.urls import path
from . import views, static


urlpatterns = [
    path("", views.home, name='home'),
    path("posts/<int:post_id>/post_detail", views.post_detail, name="post_detail"),
]