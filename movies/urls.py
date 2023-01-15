from django.urls import path
from .views import DirectorDetail, MovieDetail, MoviesList


urlpatterns = [
    path('', MoviesList.as_view(), name='home'),
    path('movies/<int:pk>', MovieDetail.as_view(), name='detail_movie'),
    path('director/<int:pk>', DirectorDetail.as_view(), name='detail_director'),
]
