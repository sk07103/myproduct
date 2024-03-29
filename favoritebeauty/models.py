from django.db import models
from django.contrib.auth import get_user_model


class MyItems(models.Model):

    name = models.CharField(max_length=50)
    user = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
    category = models.ForeignKey('categories', on_delete=models.PROTECT)
    brand = models.ForeignKey('brands', on_delete=models.PROTECT)
    price = models.IntegerField()
    rating = models.FloatField(default=0)
    regist_date = models.DateField(auto_now_add=True)
    tried = models.BooleanField(default=False)

    class Meta:
        db_table = 'myitems'

    def __str__(self):
        return self.name


class Categories(models.Model):

    code = models.CharField(max_length=3)
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


class Reviews(models.Model):

    REVIEW_CHOICES = [
        (5, '非常によい'),
        (4, 'よい'),
        (3, '普通'),
        (2, 'よくない'),
        (1, '非常によくない')
    ]

    review = models.IntegerField(choices=REVIEW_CHOICES)
    comment = models.CharField(max_length=500, blank=True, null=True)
    review_date = models.DateField()
    myitem = models.ForeignKey('myitems', on_delete=models.CASCADE)

    class Meta:
        db_table = 'reviews'
