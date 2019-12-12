from django.contrib import admin
from main.models import Anime, Temporada, Episodio, Tag, Genero

# Register your models here.

admin.site.register(Anime)
admin.site.register(Temporada)
admin.site.register(Episodio)
admin.site.register(Tag)
admin.site.register(Genero)
