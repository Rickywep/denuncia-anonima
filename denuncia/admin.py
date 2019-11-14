from django.contrib import admin
from .models import Denuncia

# Register your models here.

from import_export import resources
from import_export.admin import ImportExportModelAdmin


class DenunciaResource(resources.ModelResource):
    class Meta:
        model = Denuncia

        
@admin.register(Denuncia)
class DenunciaAdmin(ImportExportModelAdmin):
    pass

# admin.site.register(Denuncia)