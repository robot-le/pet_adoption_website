from django.contrib.auth import get_user_model
from django.db import models
from django.urls import reverse
from datetime import date


class Pet(models.Model):
    name = models.CharField(max_length=250)
    description = models.TextField(max_length=2000)
    birth_date = models.DateField(null=True, blank=True)
    breed = models.ForeignKey(
        'Breed',
        related_name='pets',
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
    )
    profile_creator = models.ForeignKey(
        get_user_model(),
        related_name='pets',
        on_delete=models.CASCADE,
    )
    organization = models.ForeignKey(
        'Organization',
        related_name='pets',
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
    )
    city = models.ForeignKey(
        'City',
        related_name='pets',
        on_delete=models.SET_NULL,
        null=True,
    )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    # media = models.ForeignKey('Media', on_delete=models.PROTECT)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('pet_detail', kwargs={'pk': self.pk})

    # def calculate_age(self):
    #     today = date.today()
    #     age = today - self.birth_date
    #     return type(self.birth_date)

    def calculate_age(self):
        years = 0
        months = 0
        if self.birth_date:
            today = date.today()
            bd = self.birth_date
            years = today.year - bd.year - ((today.month, today.day) < (bd.month, bd.day))
            months = (today.month - bd.month) % 12
            if today.day < bd.day:
                months -= 1
            if months < 0:
                months += 12
                years -= 1
        return years, months

    class Meta:
        ordering = ['created_at']


# class Media(models.Model):
#     media_file = models.FileField(upload_to='media/')
#     type = models.CharField(
#         max_length=5,
#         choices=(('image', 'Image'), ('video', 'Video'))
#     )


class Breed(models.Model):
    name = models.CharField(max_length=250)

    def __str__(self):
        return self.name


class Organization(models.Model):
    name = models.CharField(max_length=250)
    description = models.TextField(max_length=3000, null=True)
    city = models.ForeignKey('City', on_delete=models.PROTECT)
    address = models.CharField(max_length=250)
    phone = models.CharField(max_length=100)
    owner = models.OneToOneField(
        get_user_model(),
        on_delete=models.CASCADE,
        related_name='org',
    )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    # profile_image = models.ImageField()
    # worker = models.ForeignKey(
    #     get_user_model(),
    #     related_name='organizations',
    #     on_delete=models.SET_NULL,
    #     null=True,
    # )

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('organization_detail', kwargs={'pk': self.pk})

    class Meta:
        ordering = ['created_at']


class City(models.Model):
    name = models.CharField(max_length=250)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = 'Cities'
