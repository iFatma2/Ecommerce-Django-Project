from django.contrib import admin
from .models import Items, ItemDetails, Cart, ShippingAddress, Payment

# Register your models here.
admin.site.register(Items)
admin.site.register(ItemDetails)
admin.site.register(Cart)
admin.site.register(ShippingAddress)
admin.site.register(Payment)