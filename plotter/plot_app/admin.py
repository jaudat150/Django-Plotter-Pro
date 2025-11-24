from django.contrib import admin
from .models import Plot

@admin.register(Plot)
class PlotAdmin(admin.ModelAdmin):
    list_display = ('title', 'plot_type', 'created_at', 'id')
    list_filter = ('plot_type', 'created_at')
    search_fields = ('title', 'notes')
    readonly_fields = ('created_at', 'x_data', 'y_data')
    fieldsets = (
        (None, {
            'fields': ('title', 'plot_type', 'notes')
        }),
        ('Axis Labels', {
            'fields': ('x_label', 'y_label')
        }),
        ('Data', {
            'fields': ('x_data', 'y_data', 'csv_file')
        }),
        ('Media', {
            'fields': ('image',)
        }),
        ('Metadata', {
            'fields': ('created_at',),
            'classes': ('collapse',)
        }),
    )