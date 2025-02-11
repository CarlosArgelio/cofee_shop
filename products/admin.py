from django.contrib import admin

from products.models import Product


class ProductAdmin(admin.ModelAdmin):
    model = Product
    list_display = ["name", "price", "photo"]
    search_fields = ["name"]


admin.site.register(Product, ProductAdmin)
