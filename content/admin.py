from django.contrib import admin


from .models import Membros
from .models import Referencia

admin.site.register(Membros)
admin.site.register(Referencia)