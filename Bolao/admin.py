# Create your models here.

from django.contrib import admin
from .models import Jogador
from .models import Pais
from .models import Partida
from .models import Aposta

admin.site.register(Jogador)
admin.site.register(Pais)
admin.site.register(Partida)
admin.site.register(Aposta)

# Register your models here.
