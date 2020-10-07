from django.contrib import admin
from django.contrib.sitemaps.views import sitemap
from django.urls import path

from post.sitemaps import PostSitemap, StaticViewSitemap
from post.views import PostListView, PostDetailView, RobotsTxtView, AboutView

sitemaps = {
    'blog': PostSitemap,
    'static': StaticViewSitemap
}
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', PostListView.as_view(), name='posts'),
    path('about', AboutView.as_view(), name='about'),
    path('<slug:slug>', PostDetailView.as_view(), name='post'),
    path('robots.txt/', RobotsTxtView.as_view(), name='robots'),
    path('sitemap.xml', sitemap, {'sitemaps': sitemaps}),
]
