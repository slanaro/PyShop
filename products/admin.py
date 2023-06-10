from django.contrib import admin  # Import object "admin"

from .models import Product, Offer  # Import Product and other models

# Register your models here.


class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'price', 'stock')


class OfferAdmin(admin.ModelAdmin):
    list_display = ('code', 'discount')


admin.site.register(Product, ProductAdmin)        # "admin" have an attribute called "site"
                                                            # "site" is an object that call a meta called "register"
admin.site.register(Offer, OfferAdmin)
