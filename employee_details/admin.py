from django.contrib import admin
from employee_details.models import Employee

# Register your models here.

class EmployeeAdmin(admin.ModelAdmin):
    list_display=('name', 'email', 'address', 'phone')


admin.site.register(Employee, EmployeeAdmin)    