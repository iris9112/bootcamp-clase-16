from django.views.generic import ListView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from ..models import Actor


class ActorList(ListView):
    model = Actor
    ordering = "full_name"
    paginate_by = 100
    template_name = "list_actors.html"


class ActorCreate(CreateView):
    model = Actor
    fields = "__all__"


class ActorUpdate(UpdateView):
    model = Actor
    fields = ["full_name", "country_origin", "email"]


class ActorDelete(DeleteView):
    model = Actor
    success_url = reverse_lazy("actors")
