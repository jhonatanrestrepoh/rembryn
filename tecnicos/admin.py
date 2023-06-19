# models
from .models import Tecnico

# django
from django.contrib import admin
from import_export.admin import ImportExportModelAdmin  


@admin.register(Tecnico)
class TecnicoAdmin(ImportExportModelAdmin):
    pass
