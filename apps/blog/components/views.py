from django.shortcuts import render

from ..models import Post, Tag


def featured_posts(request):
    posts = Post.objects.filter(featured=True)
    return render(
        request,
        "blog/components/posts.html",
        {"posts": posts},
    )


def recent_posts(request):
    posts = Post.objects.order_by("-created_at")[:5].all()
    return render(
        request,
        "blog/components/posts.html",
        {"posts": posts},
    )


def recently_updated_posts(request):
    posts = Post.objects.order_by("-updated_at")[:5]
    return render(
        request,
        "blog/components/posts.html",
        {"posts": posts},
    )


def posts_by_tag(request, tag: str):
    posts = Tag.objects.get(name=tag).posts.all()
    return render(
        request,
        "blog/components/posts.html",
        {"posts": posts},
    )
