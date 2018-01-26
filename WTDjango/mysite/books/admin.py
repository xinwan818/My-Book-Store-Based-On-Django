from django.contrib import admin
from books.models import Publisher,Author,Book,Staff,Company,Plan

class AuthorAdmin(admin.ModelAdmin):
    list_display = ('first_name','last_name','email')
    search_fields= ('first_name','last_name')


    


class StaffAdmin(admin.ModelAdmin):
    list_display = ('first_name','last_name',)
    search_fields = ('first_name', 'last_name')
    filter_horizontal = ('plan',)
    

# Register your models here.
admin.site.register(Publisher)
admin.site.register(Author,AuthorAdmin)
admin.site.register(Book)
admin.site.register(Company)
admin.site.register(Plan)
admin.site.register(Staff,StaffAdmin)



