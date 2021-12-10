from django.contrib import admin
from .models import NbaMod, NflMod, NcaaMod

# Register your models here.

admin.site.register(NbaMod)
admin.site.register(NflMod)
admin.site.register(NcaaMod)


