from django.contrib import admin

from .models import Flat, Complaint, Owner


class OwnerAdmin(admin.ModelAdmin):
    raw_id_fields = ('flats', )


class ComplaintAdmin(admin.ModelAdmin):
    raw_id_fields = ('author', 'flat', )


class FlatAdmin(admin.ModelAdmin):
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
        'owners_phonenumber',
        'owner_pure_phone',
    ]
    list_editable = ['new_building']
    list_filter = ['new_building', 'rooms_number', 'floor']


admin.site.register(Flat, FlatAdmin)
admin.site.register(Complaint, ComplaintAdmin)
admin.site.register(Owner, OwnerAdmin)