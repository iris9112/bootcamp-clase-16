from django.contrib import admin
from .models import Actor, Director, Genre, Movie


admin.site.register(Actor)
# admin.site.register(Director)
admin.site.register(Genre)
admin.site.register(Movie)




class DirectorAdmin(admin.ModelAdmin):
    search_fields = ['full_name']

admin.site.register(Director, DirectorAdmin)
