from django.db import models
from django.contrib.auth import get_user_model


class MyItems(models.Model):

    name = models.CharField(max_length=50)
    user = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
    category = models.ForeignKey('categories', on_delete=models.PROTECT)
    brand = models.ForeignKey('brands', on_delete=models.PROTECT)
    price = models.IntegerField()
    use_start_date = models.DateField()
    rate = models.IntegerField()
    regist_date = models.DateField(auto_now=True)
    
    class Meta:
        db_table = 'my_items'
        #ordering = ['deadline']

    def __str__(self):
        return self.name

