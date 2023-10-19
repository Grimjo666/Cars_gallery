from django.contrib import admin
from bmw_description.models import SeriesDescription


class SeriesDescriptionAdmin(admin.ModelAdmin):
    list_display = ('name', 'title', 'description', 'created_at', 'updated_at')


admin.site.register(SeriesDescription, SeriesDescriptionAdmin)

