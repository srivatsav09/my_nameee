from django.contrib import admin
from cbv_app.models import School,Student,CSV
from import_export.admin import ImportExportModelAdmin


admin.site.register(School)
admin.site.register(Student)

@admin.register(CSV)
class CSVAdmin(ImportExportModelAdmin):
    list_display = ('BookId','title','author','rating')
    