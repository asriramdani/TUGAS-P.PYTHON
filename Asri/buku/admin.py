from django.contrib import admin

# Register your models here.
from . models import Post, Kategori

admin.site.register(Post)
admin.site.register(Kategori)
