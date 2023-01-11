from django.urls import path
from .views import MovieDetail, MoviesList


urlpatterns = [
    path('', MoviesList.as_view(), name='home'),
    path('movies/<int:pk>', MovieDetail.as_view(), name='detail_movie'),
]
