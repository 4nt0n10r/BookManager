from django.contrib import admin
from .models import Author, Gender, Book    
# Register your models here.

admin.site.register(Author)
admin.site.register(Gender)
admin.site.register(Book)
