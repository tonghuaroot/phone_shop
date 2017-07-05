# _*_ coding: utf-8 _*_
from django.db import models

# Create your models here.
class Maker(models.Model):
    name = models.CharField(max_length=10)
    country = models.CharField(max_length=10)

    def __unicode__(self):
        return self.name

class PModel(models.Model):
    maker = models.ForeignKey(Maker, on_delete=models.CASCADE)
    name = models.CharField(max_length=20)
    url = models.URLField(default='http://i.imgur.com/Ous4iGB.png')

    def __unicode__(self):
        return self.name

class Product(models.Model):
    pmodel = models.ForeignKey(PModel, on_delete=models.CASCADE,verbose_name='型号')
    nickename = models.CharField(max_length=15, default='超值二手机',verbose_name='摘要')
    description = models.TextField(default='暂无说明',verbose_name='描述')
    year = models.PositiveIntegerField(default=2017,verbose_name='出厂年份')
    price = models.PositiveIntegerField(default=0,verbose_name='售价')

    def __unicode__(self):
        return self.nickename

class PPhoto(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    description = models.CharField(max_length=20, default='产品照片')
    url = models.URLField(default='http://i.imgur.com/Z230eeq.png')

    def __unicode__(self):
        return self.description
