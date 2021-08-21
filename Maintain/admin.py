from django.contrib import admin
from Maintain.models.employee import Employee


class AdminEmployee(admin.ModelAdmin):
    list_display = ['first_name', 'last_name', 'email', 'phone']


# Register your models here.
admin.site.register(Employee, AdminEmployee)