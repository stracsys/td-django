from django.db import models

from django.conf import settings

from django.urls import reverse
# Create your models here.


class AbstractModel(models.Model):
    name = models.CharField(max_length=200)
    country = models.CharField(max_length=200, choices=settings.COUNTRIES)
    created_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

    class Meta:
        abstract = True
        ordering = ['name', ]


class Person(models.Model):
    name = models.CharField(max_length=200)
    age = models.PositiveIntegerField(default=0)
    sex = models.CharField(max_length=10, choices=settings.SEXE)
    country = models.CharField(max_length=200)

    def __str__(self):
        return self.name

    def isMajor(self) -> str:
        return 'Majeur' if self.age > 18 else 'Mineur'

    def get_update_url(self):
      return reverse('update', kwargs={'pk': self.id})


class Magasin(AbstractModel):
    pass


class ProfileMagasin(models.Model):
    email = models.EmailField(max_length=255,
                              unique=True,
                              verbose_name='Magasin address mail')
    phone = models.CharField(max_length=30, unique=True)
    created_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)
    magasin = models.OneToOneField(Magasin,
                                   on_delete=models.CASCADE,
                                   related_name='magasin_profile')


class Produit(AbstractModel):
    price = models.DecimalField(max_digits=10, decimal_places=2)
    image = models.ImageField(upload_to='PRODUCT_IMG')
    magasin = models.ForeignKey(Magasin,
                                on_delete=models.CASCADE,
                                related_name='product_magasin')
