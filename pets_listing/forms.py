from django import forms
from .models import (
    Pet,
    Media,
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


class MultipleFileInput(forms.ClearableFileInput):
    allow_multiple_selected = True


class MultipleFileField(forms.ImageField):

    def __init__(self, *args, **kwargs):
        kwargs.setdefault("widget", MultipleFileInput())
        super().__init__(*args, **kwargs)

    def clean(self, data, initial=None):
        single_file_clean = super().clean
        if isinstance(data, (list, tuple)):
            result = [single_file_clean(d, initial) for d in data]
        else:
            result = [single_file_clean(data, initial)]
        return result


class UploadMediaForm(forms.ModelForm):
    file = MultipleFileField(required=False)

    class Meta:
        model = Media
        fields = ['file']


class CreateOrganizationForm(forms.ModelForm):
    class Meta:
        model = Organization
        fields = ['name', 'description', 'city', 'address', 'phone']
