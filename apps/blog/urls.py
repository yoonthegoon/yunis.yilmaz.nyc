from django.urls import path

from .views import BlogDetailView, BlogListView

urlpatterns = [
    path("", BlogListView.as_view(), name="blog_list"),
    path("post/<slug:slug>/", BlogDetailView.as_view(), name="post_detail"),
]
