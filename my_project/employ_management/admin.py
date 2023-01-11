from django.contrib import admin
from .models import Employee,department,Role

# Register your models here.

admin.site.register(Employee)
admin.site.register(department)
admin.site.register(Role)
