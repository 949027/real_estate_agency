from django.contrib import admin

from .models import Flat, Complaint, Owner


class AdmineInline(admin.TabularInline):
    model = Flat.owners.through
    raw_id_fields = ('owner',)
    list_display = ['owner']


class OwnerAdmin(admin.ModelAdmin):
    list_display = ['name']
    raw_id_fields = ('flats', )


class ComplaintAdmin(admin.ModelAdmin):
    raw_id_fields = ('author', 'flat', )


class FlatAdmin(admin.ModelAdmin):
    inlines = [AdmineInline]
    raw_id_fields = ('liked_by',)
    readonly_fields = ['created_at']
    search_fields = ['town', 'owner', 'address']
    list_display_links = ['address']
    list_display = [
        'address',
        'price',
        'new_building',
        'construction_year',
        'town',
    ]
    list_editable = ['new_building']
    list_filter = ['new_building', 'rooms_number', 'floor']


admin.site.register(Flat, FlatAdmin)
admin.site.register(Complaint, ComplaintAdmin)
admin.site.register(Owner, OwnerAdmin)
