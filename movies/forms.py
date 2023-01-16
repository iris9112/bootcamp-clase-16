from django import forms
from django.core.exceptions import ValidationError

from .models import Director


class DirectorForm(forms.ModelForm):
    class Meta:
        model = Director
        fields = ("full_name", "years_experience", "biographic")

    def clean_years_experience(self):
        data = self.cleaned_data["years_experience"]
        if data <= 0:
            raise ValidationError(
                "Error: los años de experiencia no pueden ser menores a cero."
            )

        if data > 100:
            raise ValidationError("Error: los años de experiencia no corresponden")

        return data
