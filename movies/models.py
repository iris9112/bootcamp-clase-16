from django.db import models
from django.urls import reverse


class Genre(models.Model):
    name = models.CharField(max_length=100, null=False, blank=False, verbose_name="Nombre")
    created = models.DateTimeField(auto_now_add=True, verbose_name="Fecha de creación")
    updated = models.DateTimeField(auto_now=True, verbose_name="Fecha de edición")

    class Meta:
        verbose_name = "Genero"
        verbose_name_plural = "Generos"
        ordering = ["name"]

    def __str__(self):
        return self.name


class Director(models.Model):
    full_name = models.CharField(max_length=100, null=False, blank=False, verbose_name="Nombre Completo")
    years_experience = models.SmallIntegerField(default=1, verbose_name="Años de experiencia")
    biographic = models.TextField(null=True, blank=True, verbose_name="Resumen")
    created = models.DateTimeField(auto_now_add=True, verbose_name="Fecha de creación")
    updated = models.DateTimeField(auto_now=True, verbose_name="Fecha de edición")

    class Meta:
        verbose_name = "Director"
        verbose_name_plural = "Directores"
        ordering = ["-created"]

    def __str__(self):
        return f"{self.full_name} - {self.years_experience}"

    def get_absolute_url(self):
        """
         Devuelve la url para acceder a una instancia particular del modelo.
        """
        return reverse('detail_director', args=[str(self.id)])

    @property
    def movies(self):
        return self.movie_set.all()

    def get_movies_by_year(self, year):
        return self.movie_set.filter(released_year=year)


class Actor(models.Model):
    full_name = models.CharField(max_length=100, null=False, blank=False, verbose_name="Nombre Completo")
    country_origin = models.CharField(max_length=100, null=True, blank=True, verbose_name="País Origen")
    email = models.EmailField(blank=True)
    created = models.DateTimeField(auto_now_add=True, verbose_name="Fecha de creación")
    updated = models.DateTimeField(auto_now=True, verbose_name="Fecha de edición")

    class Meta:
        verbose_name = "Actor"
        verbose_name_plural = "Actores"
        ordering = ["full_name"]

    def __str__(self):
        return self.full_name


class Movie(models.Model):
    TYPE_CERTIFICATE = [
        ('u', 'U'),
        ('a', 'A'),
        ('ua', 'UA'),
        ('r', 'R'),
        ('pg-13', 'PG-13'),
        ('other', 'Other'),
    ]

    title = models.CharField(max_length=150, null=False, blank=False, verbose_name="Título")
    overview = models.TextField(null=True, blank=True, verbose_name="Resumen")
    released_year = models.IntegerField(null=True, blank=True, verbose_name="Año lanzamiento")
    certificate = models.CharField(max_length=6, choices=TYPE_CERTIFICATE, null=True, blank=True, verbose_name="Certificado")
    runtime = models.IntegerField(help_text="Duración de la película en minutos", verbose_name="Duración")
    genre = models.ManyToManyField(Genre, related_name="get_genres", verbose_name="Genero")
    rating = models.FloatField(default=1.0, null=True,verbose_name="Raiting IMDB")
    director = models.ForeignKey(Director, on_delete=models.SET_NULL, null=True)
    actores = models.ManyToManyField(Actor, related_name="get_actores")
    gross = models.PositiveIntegerField(default=0, verbose_name="Recaudo")
    created = models.DateTimeField(auto_now_add=True, verbose_name="Fecha de creación")
    updated = models.DateTimeField(auto_now=True, verbose_name="Fecha de edición")

    class Meta:
        verbose_name = "Película"
        verbose_name_plural = "Películas"
        ordering = ["-rating"]

    def __str__(self):
        return f"{self.title}: {self.released_year}"

    def get_absolute_url(self):
        return reverse('detail_movie', args=[str(self.id)])

    def get_brochure(self):
        msg = f"La película {self.title}: "

        if self.director:
            msg += f"dirigida por {self.director.full_name}, "

        if self.released_year:
            msg += f"fue lanzada en el año {self.released_year}"

        if self.gross > 0:
            msg += f". Recaudando un total de: ${self.gross:,.2f}"

        return msg
