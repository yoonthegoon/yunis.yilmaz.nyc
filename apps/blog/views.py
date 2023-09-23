from django.shortcuts import redirect, render

from .models import Post, Tag


def index(request):
    return render(request, "blog/index.html")


def post_detail(request, year: int, month: int, slug: str):
    post = Post.objects.filter(created_at__year=year, created_at__month=month).get(
        slug=slug
    )
    return render(request, "blog/post.html", {"post": post})


def write_post(request):
    if request.method == "POST":
        post = Post.objects.create(
            title=request.POST["title"], content=request.POST["content"]
        )
        return redirect(post.url)

    return render(request, "blog/write_post.html")


def tag_detail(request, name: str):
    tag = Tag.objects.get(name=name)
    return render(request, "blog/tag.html", {"tag": tag.name})
