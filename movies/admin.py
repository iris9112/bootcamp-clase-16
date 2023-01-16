from django.contrib import admin
from .models import Actor, Director, Genre, Movie


admin.site.register(Actor)
admin.site.register(Genre)


class DirectorAdmin(admin.ModelAdmin):
    search_fields = ["full_name"]


admin.site.register(Director, DirectorAdmin)


class MovieAdmin(admin.ModelAdmin):
    search_fields = ["title", "released_year", "certificate", "rating", "genre__name"]
    list_filter = ("certificate", "genre__name")


admin.site.register(Movie, MovieAdmin)
