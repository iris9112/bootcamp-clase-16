from django.views.generic import ListView, DetailView
from django.views.generic.base import TemplateView
from django.views.generic.edit import DeleteView, UpdateView
from django.urls import reverse_lazy
from ..models import Movie


class Home(TemplateView):
    template_name = "home.html"


class MoviesList(ListView):
    model = Movie
    ordering = "-rating"
    paginate_by = 100
    template_name = "list_movies.html"
    context_object_name = "movies"


class MovieDetail(DetailView):
    model = Movie
    template_name = "detail_movie.html"
    context_object_name = "movie"


class MovieUpdate(UpdateView):
    model = Movie
    template_name = "movie_form.html"
    fields = "__all__"


class MovieDelete(DeleteView):
    model = Movie
    success_url = reverse_lazy("list_movies")
    template_name = "confirm_delete.html"
