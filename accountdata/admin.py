from django.contrib import admin
from .models import Blog,Blogcomment
# Register your models here.
admin.site.register((Blog,Blogcomment))