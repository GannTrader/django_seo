from django.contrib.sitemaps import ping_google
from django.db import models
from django.urls import reverse
from django.utils.text import slugify


class Post(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField(blank=True, null=True)
    slug = models.SlugField(unique=True, blank=True, null=True)
    body = models.TextField()

    def __str__(self):
        return self.title

    def save(self, force_insert=None, force_update=None):
        self.slug = slugify(self.title)
        super(Post, self).save(force_insert, force_update)
        try:
            ping_google()
        except Exception:
            pass

    def get_absolute_url(self, *args, **kwargs):
        return reverse("post", args=[str(self.slug)])