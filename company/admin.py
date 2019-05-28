from django.contrib import admin
from .models import Company, Position, Personal, Rating

# admin.site.register(Company)
class CompanyAdmin(admin.ModelAdmin):
    list_display = ('name', 'inn', 'ogrn', 'kpp', 'address', 'post_address', 'phone', 'name_director', 'last_name_director')
admin.site.register(Company,CompanyAdmin)

# class PositionAdmin(admin.ModelAdmin):
#     list_display = ('position')
# admin.site.register(Position,PositionAdmin)
#
admin.site.register(Position)

# class PersonalAdmin(admin.ModelAdmin):
#     list_display = ('first_name', 'last_name', 'phone', 'email', 'position')
# admin.site.register(Personal,PersonalAdmin)

admin.site.register(Personal)

class RatingAdmin(admin.ModelAdmin):
    list_display = ('id', 'rating')
admin.site.register(Rating,RatingAdmin)




