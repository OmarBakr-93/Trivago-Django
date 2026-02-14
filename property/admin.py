from django.contrib import admin
from .models import Property, Property_book, Property_Review, property_images, Place, Category
from django_summernote.admin import SummernoteModelAdmin

# Register your models here.

class SomeModelAdmin(SummernoteModelAdmin): 
    summernote_fields = '__all__'
    list_display= ['name' , 'price', 'check_availability' , 'get_avg_rating']
admin.site.register(Property, SomeModelAdmin)

class propertyBookAdmin(admin.ModelAdmin): 
    list_display = ['property', 'in_progress']
admin.site.register(Property_book, propertyBookAdmin)

admin.site.register(Property_Review)
admin.site.register(property_images)
admin.site.register(Place)
admin.site.register(Category)
