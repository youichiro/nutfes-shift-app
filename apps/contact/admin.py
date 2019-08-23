from django.contrib import admin
from markdownx.admin import MarkdownxModelAdmin
from apps.contact.models import Contact


admin.site.register(Contact, MarkdownxModelAdmin)
