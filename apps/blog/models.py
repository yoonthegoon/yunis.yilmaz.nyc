from datetime import timedelta

from django.db import models
from django.urls import reverse


class Post(models.Model):
    title = models.CharField(max_length=255)
    body = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    featured = models.BooleanField(default=False)
    tags = models.ManyToManyField("Tag", related_name="posts", blank=True)
    slug = models.SlugField(blank=True, unique=True)

    @property
    def excerpt(self):
        return self.body[:96].replace("#", "").lstrip() + "..."

    @property
    def url(self):
        return reverse(
            "post",
            kwargs={
                "year": self.created_at.year,
                "month": self.created_at.month,
                "slug": self.slug,
            },
        )
    
    def pre_save(self):
        self.slug = self.title.replace(" ", "-").lower()

    def save(self, *args, **kwargs):
        self.pre_save()
        super().save(*args, **kwargs)

    def __str__(self):
        return self.title


class Tag(models.Model):
    name = models.CharField(max_length=255, unique=True)

    @property
    def url(self):
        return reverse("tag", kwargs={"name": self.name})

    def __str__(self):
        return self.name
