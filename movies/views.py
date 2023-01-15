from django.views.generic import ListView, DetailView
from .models import Movie, Director


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


class DirectorDetail(DetailView):
    model = Director
    template_name = 'detail_director.html'

    def get_context_data(self, **kwargs):
        context = super(DirectorDetail, self).get_context_data(**kwargs)
        context['best_movie'] = self.object.movie_set.order_by('-gross').values('id', 'title', 'gross')[0]
        return context
