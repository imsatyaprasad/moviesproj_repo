from django.contrib import admin
from .models import Movie
# Register your models here.
class MovieAdmin(admin.ModelAdmin):
    list_display = ['moviename','hero','heroine','rating']

admin.site.register(Movie,MovieAdmin)