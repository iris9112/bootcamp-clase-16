from django.views.generic import ListView, DetailView
from .models import Movie


class MoviesList(ListView):
    model = Movie
    ordering = '-rating'
    paginate_by = 100
    template_name = 'list_movies.html'
    context_object_name = 'movies'  # object_list


class MovieDetail(DetailView):
    model = Movie
    template_name = 'detail_movie.html'
    context_object_name = 'movie'  # object
