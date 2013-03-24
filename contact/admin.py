from django.contrib import admin
from contact.models import Contact


class ContactAdmin(admin.ModelAdmin):
    list_display = ('name', 'phone', 'email', 'message')
    search_fields = ('name', 'phone', 'email', 'message')

admin.site.register(Contact, ContactAdmin)

