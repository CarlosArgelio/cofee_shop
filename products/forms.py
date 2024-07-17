# Forms
from django import forms
from django.forms import CharField, DecimalField, BooleanField, ImageField

from products.models import Product


class ProductForm(forms.Form):
    name = CharField(max_length=200, label="Nombre")
    description = CharField(max_length=200, label="Descripcion")
    price = DecimalField(max_digits=10, decimal_places=2, label="Precio")
    available = BooleanField(initial=True, label="Disponible", required=False)
    photo = ImageField(label="Foto", required=False)

    def save(self):
        Product.objects.create(
            name=self.cleaned_data["name"],
            description=self.cleaned_data["description"],
            price=self.cleaned_data["price"],
            available=self.cleaned_data["available"],
            photo=self.cleaned_data["photo"],
        )
