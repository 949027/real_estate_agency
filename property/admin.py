from django.contrib import admin

from .models import Flat, Complaint


class ComplaintAdmin(admin.ModelAdmin):
    raw_id_fields = ('author', 'flat', )


class FlatAdmin(admin.ModelAdmin):
    readonly_fields = ['created_at']
    search_fields = ['town', 'owner', 'address']
    list_display_links = None
    list_display = [
        'address',
        'price',
        'new_building',
        'construction_year',
        'town'
    ]
    list_editable = ['new_building']
    list_filter = ['new_building', 'rooms_number', 'floor']


admin.site.register(Flat, FlatAdmin)
admin.site.register(Complaint, ComplaintAdmin)