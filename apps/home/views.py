from django.shortcuts import render

from apps.blog.models import Post


def index(request):
    context = {"title": "Home"}
    return render(request, "home/index.html", context)
