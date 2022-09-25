from django.contrib import admin
from .models import TestModel,Modelx,UserModel

# Register your models here.
admin.site.register((TestModel,Modelx,UserModel))