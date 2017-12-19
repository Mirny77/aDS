from django.db import models
from goods.models import Goods


class Status(models.Model):
    name = models.CharField(max_length=24, blank=True, null=True, default=None)
    is_active = models.BooleanField(default=True)
    created = models.DateTimeField(auto_now_add=True, auto_now=False)
    updated = models.DateTimeField(auto_now_add=False, auto_now=True)

    def __str__(self):
        return "Статус %s" % self.name

    class Meta:
        verbose_name = 'Статус продавца'
        verbose_name_plural = 'Статусы продавца'

class Seller(models.Model):
    name=models.CharField(max_length=64)
    phone=models.CharField(max_length=15)
    email=models.EmailField(max_length=64,null=True, default=None)
    status=models.ForeignKey(Status)

    goods=models.ForeignKey(Goods)
    created = models.DateTimeField(auto_now_add=True, auto_now=False)
    updated = models.DateTimeField(auto_now_add=False, auto_now=True)

    def __str__(self):
        return "%s" % self.name

    class Meta:
        verbose_name = 'Продавец'

        verbose_name_plural = 'Продавцы'





