from django.contrib import admin
from .models import *
class SellerAdmin (admin.ModelAdmin):
    list_display = [field.name for field in Seller._meta.fields]
    
    


    class Meta:
        model = Seller

admin.site.register(Seller, SellerAdmin)


class StatusAdmin (admin.ModelAdmin):
    list_display = [field.name for field in Status._meta.fields]

    class Meta:
        model = Status

admin.site.register(Status, StatusAdmin)
