from django.contrib import admin
from .models import About, FAQ
from django_summernote.admin import SummernoteModelAdmin

# Register your models here.

class SomeModelAdmin(SummernoteModelAdmin): 
    summernote_fields = '__all__'
    
admin.site.register(About, SomeModelAdmin)
admin.site.register(FAQ, SomeModelAdmin)