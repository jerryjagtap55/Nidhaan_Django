from django.contrib import admin
from .models import ContactUs
# Register your models here.

class ContactUsAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')
    list_display_links = ('id', 'name')
    list_per_page = 5

admin.site.register(ContactUs, ContactUsAdmin)