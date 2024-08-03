from django.contrib import admin

# Register your models here.

from signup.models import signup

class signupAdmin(admin.ModelAdmin):
    list_display=('username', 'passward')

admin.site.register(signup,signupAdmin)    