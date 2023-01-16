from django.contrib.auth.mixins import PermissionRequiredMixin, LoginRequiredMixin
from django.contrib import messages
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, DeleteView, UpdateView
from django.urls import reverse_lazy
from ..forms import DirectorForm
from ..models import Director


class DirectorList(ListView):
    model = Director
    ordering = "full_name"
    paginate_by = 100
    template_name = "list_directors.html"


class DirectorDetail(DetailView):
    model = Director
    template_name = "detail_director.html"

    def get_context_data(self, **kwargs):
        context = super(DirectorDetail, self).get_context_data(**kwargs)
        movies = self.object.movie_set.order_by("-gross").values("id", "title", "gross")
        if movies:
            context["best_movie"] = movies[0]

        return context


class DirectorCreate(CreateView):
    model = Director
    template_name = "director_form.html"
    form_class = DirectorForm


class DirectorUpdate(PermissionRequiredMixin, UpdateView):
    model = Director
    template_name = "director_form.html"
    fields = ["full_name", "years_experience", "biographic"]
    permission_required = "director.change_choice"


class DirectorDelete(DeleteView):
    model = Director
    success_url = reverse_lazy("list_directors")
    template_name = "confirm_delete.html"
