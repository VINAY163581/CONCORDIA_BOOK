from django.contrib import admin

# Register your models here.

# bookexchange/admin.py
from django.contrib import admin
from Textbooks.models import Textbook
 
# Register the Textbook model to make it available in the admin interface
admin.site.register(Textbook)