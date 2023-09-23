from django.urls import path

from .views import featured_posts, posts_by_tag, recent_posts, recently_updated_posts

urlpatterns = [
    path("featured-posts/", featured_posts, name="featured_posts"),
    path("recent-posts/", recent_posts, name="recent_posts"),
    path(
        "recently-updated-posts/", recently_updated_posts, name="recently_updated_posts"
    ),
    path("posts-by-tag/<str:tag>", posts_by_tag, name="posts_by_tag"),
]
