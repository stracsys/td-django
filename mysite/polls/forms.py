from django import forms
from polls.models import *

from django.conf import settings


class PersonForm(forms.ModelForm):
    name = forms.CharField(
        required=True,
        max_length=200,
        strip=True,
        min_length=2,
        widget=forms.TextInput(
            attrs={
                'type': 'text'
            }
        )
    )

    age = forms.CharField(
        required=True,
        max_length=200,
        strip=True,
        min_length=2,
        widget=forms.NumberInput(
            attrs={
                'type': 'number'
            }
        )
    )

    sex = forms.ChoiceField(
        required=True,
        choices=[(x, y) for (x, y) in settings.SEXE],
        widget=forms.Select(
            attrs={
                'type': 'select'
            }
        )
    )

    country = forms.ChoiceField(
        required=True,
        choices=[(x, y) for (x, y) in settings.COUNTRIES],
        widget=forms.Select(
            attrs={
                'type': 'select'
            }
        )
    )

    class Meta:

        model = Person

        fields = [
            'name',
            'age',
            'sex',
            'country',
        ]


class MagasinForm(forms.ModelForm):

    class Meta:
        model = Magasin
        # fields = [all]
        fields = [
            'name',
            'country',
            # 'created_at',
            # 'update_at'
        ]


class ProfileMagasinForm(forms.ModelForm):
    class Meta:
        model = ProfileMagasin
        fields = [
            'email',
            'phone',
            'magasin'
        ]


class ProduitForm(forms.ModelForm):
    class Meta:
        model = Produit
        fields = [
            'name',
            'country',
            'price',
            # 'image',
            'magasin'
        ]
