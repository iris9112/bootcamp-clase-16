from django.contrib.auth.models import User
from django.test import TestCase
from django.urls import reverse
from model_mommy import mommy
from ..models import Movie


class MoviesViewsTest(TestCase):

    def setUp(self):
        self.password = "12345"
        self.test_user = User.objects.create_user(
            username="test_user", password=self.password, is_superuser=True, is_staff=True
        )
        self.test_user.save()

        self.movie = mommy.make(Movie, certificate="a", gross=12012455, director__full_name="John Doe")
        # https://model-mommy.readthedocs.io/en/latest/basic_usage.html

    def test_view_url_exists_at_desired_location(self):
        resp = self.client.get("/movies")
        self.assertEqual(resp.status_code, 200)

    def test_view_url_accessible_by_name(self):
        resp = self.client.get(reverse("list_movies"))
        self.assertEqual(resp.status_code, 200)

    def test_view_uses_correct_template(self):
        resp = self.client.get(reverse("list_movies"))
        self.assertEqual(resp.status_code, 200)
        self.assertTemplateUsed(resp, "list_movies.html")

    def test_view_not_movies_to_show(self):
        Movie.objects.all().delete()
        response = self.client.get("/movies")
        self.assertContains(response, "No hay peliculas disponibles")
        self.assertEqual(response.status_code, 200)

    def test_view_contains_title_of_movie(self):
        response = self.client.get("/movies")
        self.assertContains(response, self.movie.__str__())
        self.assertEqual(response.status_code, 200)
        self.assertFalse(response.context_data["is_paginated"])
        self.assertTrue(len(response.context["object_list"]) == 1)

    def test_delete_movie(self):
        response = self.client.post("/movies/delete/1")
        self.assertEqual(response.status_code, 302)
        self.assertFalse(Movie.objects.count())

        resp = self.client.get(reverse("list_movies"))
        assert resp.template_name[0] == "list_movies.html"

    def test_movie_not_found(self):
        response = self.client.get("/movies/1584")
        self.assertEqual(response.status_code, 404)

    def test_message_in_template_content(self):
        self.client.login(username=self.test_user.username, password=self.password)
        response = self.client.get(reverse("list_movies"))
        self.assertContains(response, "Crear Pelicula")
