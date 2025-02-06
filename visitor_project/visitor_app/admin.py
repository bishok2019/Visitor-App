from django.contrib import admin
from .models import CustomUser, Department, Visitor
# Register your models here.
admin.site.register(CustomUser)
admin.site.register(Department)
admin.site.register(Visitor)