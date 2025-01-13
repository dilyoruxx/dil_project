from django.contrib import admin

from apps.base.models import Book, About

# Register your models here.

admin.site.register(Book)
admin.site.register(About)