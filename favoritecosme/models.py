from django.db import models
from django.contrib.auth import get_user_model


class MyItems(models.Model):

    name = models.CharField(max_length=50)
    user = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
    category = models.ForeignKey('categories', on_delete=models.PROTECT)
    brand = models.ForeignKey('brands', on_delete=models.PROTECT)
    price = models.IntegerField()
    regist_date = models.DateField(auto_now=True)
    tried = models.BooleanField(default=False)

    class Meta:
        db_table = 'my_items'
        #ordering = ['deadline']

    def __str__(self):
        return self.name
    

class Categories(models.Model):

    code = models.CharField(max_length=3, min_length=3)
    name = models.CharField(max_length=100)

    class Meta:
        db_table = 'categories'

    def __str__(self):
        return self.name


class Brands(models.Model):

    name = models.CharField(max_length=100)

    class Meta:
        db_table = 'brands'
    
    def __str__(self):
        return self.name
