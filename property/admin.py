from django.contrib import admin

from .models import Flat, Complaint, Owner


class OwnersInline(admin.TabularInline):
    model = Flat.owners.through
    raw_id_fields = ['owner', 'flat']


class FlatAdmin(admin.ModelAdmin):
    search_fields = ['town', 'address', 'owner']
    readonly_fields = ['created_at']
    list_display = ['address', 'price', 'new_building', 'construction_year',
                    'town']
    list_editable = ['new_building']
    list_filter = ['new_building', 'rooms_number', 'has_balcony']
    raw_id_fields = ['likes']

    inlines = [
        OwnersInline
    ]


class CompliantAdmin(admin.ModelAdmin):
    raw_id_fields = ('user', 'flat')


class OwnerAdmin(admin.ModelAdmin):
    raw_id_fields = ['flats']
    search_fields = ['name']


admin.site.register(Flat, FlatAdmin)
admin.site.register(Complaint, CompliantAdmin)
admin.site.register(Owner, OwnerAdmin)

