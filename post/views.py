from django.views.generic import ListView, DetailView, TemplateView

from post.models import Post


class PostListView(ListView):
    model = Post
    template_name = "posts.html"


class PostDetailView(DetailView):
    model = Post
    template_name = "post.html"

    def get_object(self, queryset=None, **kwargs):
        _slug = self.kwargs["slug"]
        _post = Post.objects.get(slug=_slug)
        return _post


class RobotsTxtView(TemplateView):
    template_name = "robots.txt"


class AboutView(TemplateView):
    template_name = "about.html"
