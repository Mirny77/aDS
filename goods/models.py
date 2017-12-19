from django.db import models


class GoodsCategory(models.Model):
    name = models.CharField(max_length=64, blank=True, null=True, default=None)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return "%s" % self.name

    class Meta:
        verbose_name = 'Категория товара'
        verbose_name_plural = 'Категория товаров'


class Goods(models.Model):
    headline=models.CharField(max_length=64,default=None,blank=True,null=True)

    category = models.ForeignKey(GoodsCategory, blank=True, null=True, default=None)
    price=models.DecimalField(max_digits=10, decimal_places=2, default=0)
    short_description = models.TextField(blank=True, null=True, default=None)
    description = models.TextField(blank=True, null=True, default=None)
    is_active = models.BooleanField(default=True)
    created = models.DateTimeField(auto_now_add=True, auto_now=False)
    updated = models.DateTimeField(auto_now_add=False, auto_now=True)


    def __str__(self):
        return "%s" % self.headline

    class Meta:
        verbose_name = 'Объявление'


        verbose_name_plural = 'Объявления'





class GoodsImage(models.Model):
    goods=models.ForeignKey(Goods,blank=True, null=True, default=None)
    image=models.ImageField(upload_to='goods_img/')
    is_main = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)

    created = models.DateTimeField(auto_now_add=True, auto_now=False)
    updated = models.DateTimeField(auto_now_add=False, auto_now=True)

    def __str__(self):
        return "%s" % self.id

    class Meta:
        verbose_name = 'Фотография'
        verbose_name_plural = 'Фотографии'




class Address(models.Model):
    goods = models.ForeignKey(Goods, blank=True, null=True, default=None)
    country=models.CharField(max_length=64)
    sity=models.CharField(max_length=64)
    district=models.CharField(max_length=64,blank=True, null=True, default=None)
    street=models.CharField(max_length=64,blank=True, null=True, default=None)
    house=models.CharField(max_length=64,blank=True, null=True, default=None)

    def __str__(self):
        return "%s" % self.sity

    class Meta:
        verbose_name = 'Адрес'

        verbose_name_plural = 'Адреса'




