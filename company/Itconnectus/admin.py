from django.contrib import admin
from .models import Client, Role, Employee
# Register your models here.

admin.site.register(Client)
admin.site.register(Role)
admin.site.register(Employee)
