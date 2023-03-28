from django.contrib import admin
from .models import MyItems, Categories, Brands, Reviews

admin.site.register(MyItems)
admin.site.register(Categories)
admin.site.register(Brands)
admin.site.register(Reviews)
