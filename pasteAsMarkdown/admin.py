from django.contrib import admin
from .models import Markdown, MarkdownAdmin

# Register your models here.

admin.site.register(Markdown, MarkdownAdmin)
