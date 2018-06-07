from django.conf.urls import url
from . import views as posts_views
from django.views.generic import ListView, DetailView
from .models import posts

# lista dei post | homepage
# post singoli dei blog
# sezione contatti
urlpatterns = [
    url(r'^$', ListView.as_view(
        queryset = posts.objects.all().order_by("-data"),
        template_name = "lista_post.html",
        paginate_by = 5),
    name="lista"),

    url(r'^(?P<id>\d+)/(?P<slug>[\w-]+)/$', DetailView.as_view(
        model = posts,
        template_name = "post_singolo.html"), name="singolo"),

    url(r'^contatti/$', posts_views.contatti, name="contatti"),
]