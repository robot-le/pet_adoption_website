from django import forms
from .models import (
    Pet,
    Organization,
)


class DateInput(forms.DateInput):
    input_type = 'date'


class CreatePetProfileForm(forms.ModelForm):
    class Meta:
        model = Pet
        fields = ['name', 'description', 'birth_date', 'breed', 'city']
        widgets = {
            'birth_date': DateInput(),
        }

    # def clean_title(self):
    #     title = self.cleaned_data['title']
    #     if len(title) > 50:
    #         raise ValidationError("Длина превышает 50 символов")
    #
    #     return title


class CreateOrganizationForm(forms.ModelForm):
    class Meta:
        model = Organization
        fields = ['name', 'description', 'city', 'address', 'phone']
