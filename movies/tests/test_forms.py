from django.test import TestCase
from ..forms import DirectorForm


class DirectorFormTest(TestCase):

    def test_director_form_years_experience_less_than_zero(self):
        form_data = {"full_name": "Aureliano Buendia", "years_experience": -15}
        form = DirectorForm(data=form_data)
        self.assertFalse(form.is_valid())
        self.assertEqual(
            form._errors['years_experience'][0],
            "Error: los años de experiencia no pueden ser menores a cero."
        )
