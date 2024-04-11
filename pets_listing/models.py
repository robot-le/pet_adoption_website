from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User


class Pet(models.Model):
    name = models.CharField(max_length=250)
    description = models.TextField(max_length=2000)
    birth_date = models.DateField(null=True, blank=True)
    breed = models.ForeignKey(
        'Breed',
        related_name='pets',
        on_delete=models.SET_NULL,
        null=True,
    )
    profile_creator = models.ForeignKey(
        User,
        related_name='pets',
        on_delete=models.CASCADE,
    )
    organization = models.ForeignKey(
        'Organization',
        related_name='pets',
        on_delete=models.SET_NULL,
        null=True,
    )
    city = models.ForeignKey(
        'City',
        related_name='pets',
        on_delete=models.SET_NULL,
        null=True,
    )

    # media = models.ForeignKey('Media', on_delete=models.PROTECT)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('pet-detail', kwargs={'pk': self.pk})


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
    owner = models.OneToOneField(User, on_delete=models.CASCADE)
    # worker = models.ForeignKey(
    #     User,
    #     related_name='organizations',
    #     on_delete=models.SET_NULL,
    #     null=True,
    # )

    def __str__(self):
        return self.name


class City(models.Model):
    name = models.CharField(max_length=250)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = 'Cities'
