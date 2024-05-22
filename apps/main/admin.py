from django.contrib import admin
from .models import Contact
# Register your models here.


@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'email', 'subject', 'created_date',)
    readonly_fields = ('created_date',)
    list_filter = ('name', 'email',)
    date_hierarchy = 'created_date'
    list_display_links = ('id', 'name', 'email', 'subject', 'created_date',)