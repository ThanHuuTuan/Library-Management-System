from django.contrib import admin
from .models import User, Book_Issue, Books_Details

# Register your models here.
admin.site.register(User)
admin.site.register(Book_Issue)
admin.site.register(Books_Details)
