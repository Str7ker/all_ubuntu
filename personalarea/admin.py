from django.contrib import admin
from .models import Personalarea, New_personal

class New_personalAdmin(admin.ModelAdmin):
    list_display = ('login', 'password', 'email', 'first_name', 'last_name', 'phone')
admin.site.register(New_personal,New_personalAdmin)

# admin.site.register(New_personal)

# class PersonalareaAdmin(admin.ModelAdmin):
#     list_display = ('login', 'password', 'email', 'first_name', 'last_name', 'phone', 'position')
# admin.site.register(Personalarea,PersonalareaAdmin)

admin.site.register(Personalarea)
