from django.urls import path
from .views.views_actors import ActorList
from .views.views_directors import (
    DirectorList,
    DirectorDetail,
    DirectorCreate,
    DirectorUpdate,
    DirectorDelete,
)
from .views.views_movies import Home, MoviesList, MovieDetail, MovieUpdate, MovieDelete


urlpatterns = [
    path("", Home.as_view(), name="home"),
    path("movies", MoviesList.as_view(), name="list_movies"),
    path("movies/<int:pk>", MovieDetail.as_view(), name="detail_movie"),
    path("movies/update/<int:pk>", MovieUpdate.as_view(), name="update_movie"),
    path("movies/delete/<int:pk>", MovieDelete.as_view(), name="delete_movie"),
    path("director/", DirectorList.as_view(), name="list_directors"),
    path("director/<int:pk>", DirectorDetail.as_view(), name="detail_director"),
    path("director/create", DirectorCreate.as_view(), name="create_director"),
    path("director/update/<int:pk>", DirectorUpdate.as_view(), name="update_director"),
    path("director/delete/<int:pk>", DirectorDelete.as_view(), name="delete_director"),
    path("actors/", ActorList.as_view(), name="list_actors"),
]
