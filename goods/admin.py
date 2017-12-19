from django.contrib import admin
from .models import *


class GoodsImageInline(admin.TabularInline):
    model = GoodsImage
    extra = 0
class AddressInline(admin.TabularInline):
    model = Address
    extra = 0


class GoodsCategoryAdmin(admin.ModelAdmin):
    list_display = [field.name for field in GoodsCategory._meta.fields]

    class Meta:
        model = GoodsCategory

admin.site.register(GoodsCategory, GoodsCategoryAdmin)


class GoodsAdmin (admin.ModelAdmin):
    list_display = [field.name for field in Goods._meta.fields]
    inlines = [GoodsImageInline,AddressInline]


    class Meta:
        model = Goods

admin.site.register(Goods, GoodsAdmin)


class GoodsImageAdmin (admin.ModelAdmin):
    list_display = [field.name for field in GoodsImage._meta.fields]

    class Meta:
        model = GoodsImage

admin.site.register(GoodsImage, GoodsImageAdmin)

class AddressAdmin(admin.ModelAdmin):
    list_display = [field.name for field in Address._meta.fields]

    class Meta:
        model = Address

admin.site.register(Address, AddressAdmin)
