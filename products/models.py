# Models
from django.db import models
from django.db.models import TextField, DecimalField, BooleanField, ImageField


class Product(models.Model):
    name = TextField(max_length=200, verbose_name="nombre")
    description = TextField(max_length=300, verbose_name="descripcion")
    price = DecimalField(max_digits=10, decimal_places=2, verbose_name="precio")
    available = BooleanField(default=True, verbose_name="disponible")
    photo = ImageField(upload_to="logos", null=True, blank=True, verbose_name="foto")

    def __str__(self) -> str:
        return self.name
