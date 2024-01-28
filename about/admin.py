from django.contrib import admin
from django_summernote.admin import SummernoteModelAdmin
from .models import About, ContactRequest


@admin.register(About)
class AboutAdmin(SummernoteModelAdmin):
    """
    Adds rich-text editing of the content whilst in the admin panel.
    """
    summernote_fields = ('content',)

# Register your models here.


@admin.register(ContactRequest)
class ContactRequestAdmin(admin.ModelAdmin):
    """
    Gives a list of messages and read fields in the admin panel.
    """
    list_display = ('message', 'read',)
