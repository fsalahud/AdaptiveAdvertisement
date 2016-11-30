from django.contrib import admin

# Register your models here.
from .models import User, Poster, Image

admin.site.register(User)
admin.site.register(Poster)
admin.site.register(Image)