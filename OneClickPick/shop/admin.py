from django.contrib import admin
from .models import Product,Contact,Order,OrderUpdate
# Register your models here.
'''as mentioned in the command above, whatever tables we are creating inside the models.py file, we have to register
over here'''
admin.site.register(Product)
admin.site.register(Contact)
admin.site.register(Order)
admin.site.register(OrderUpdate)
