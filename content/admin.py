from django.contrib import admin


from .models import Membros
from .models import Referencia
from .models import Duvidas

admin.site.register(Membros)
admin.site.register(Referencia)
admin.site.register(Duvidas)