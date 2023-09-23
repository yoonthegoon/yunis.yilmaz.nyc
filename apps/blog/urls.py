from django.urls import include, path

from .views import index, post_detail, tag_detail, write_post

urlpatterns = [
    path("", index, name="index"),
    path("posts/<int:year>/<int:month>/<slug:slug>", post_detail, name="post"),
    # path("write-post/", write_post, name="write_post"),
    path("tag/<str:name>", tag_detail, name="tag"),
    path("components/", include("apps.blog.components.urls")),
]
