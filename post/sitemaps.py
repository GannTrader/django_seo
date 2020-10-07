from django.contrib.sitemaps import Sitemap
from django.urls import reverse

from post.models import Post


class PostSitemap(Sitemap):
    def items(self):
        return Post.objects.all()


class StaticViewSitemap(Sitemap):
    def items(self):
        return ['about']

    def location(self, item):
        return reverse(item)