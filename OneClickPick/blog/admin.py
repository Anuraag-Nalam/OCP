
from django.contrib import admin
from .models import Blogpost
# Register your models here.
'''as mentioned in the command above, whatever tables we are creating inside the models.py file, we have to register
over here'''
admin.site.register(Blogpost)
