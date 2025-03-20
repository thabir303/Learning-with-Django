#query_optimization/library/admin.py
from django.contrib import admin
from .models import *
# Register your models here.

admin.site.register(CustomUser)
admin.site.register(Author)
admin.site.register(Publisher)
admin.site.register(Book)
admin.site.register(BookReview)
admin.site.register(Genre)
admin.site.register(BookGenre)