from django.contrib import admin
from daterange_filter.filter import DateRangeFilter

from import_export.admin import ImportExportModelAdmin

from .models import Flat, Photo


class PhotoInline(admin.TabularInline):
    model = Photo
    extra = 0

class FlatAdmin(ImportExportModelAdmin):
    list_display = ('available_from', 'licensor', 'property', 'post_code',
                    'area', 'n_b', 'price_one', 'price_two',
                    'upfront', 'bills', 'min_length')
    list_filter = ('area', ('available_from', DateRangeFilter), 'licensor',
                    'property', 'post_code', 'price_one', 'price_two',
                    'n_b')
    search_fields = ('licensor', 'property', 'area', 'n_b',
                     'price_one', 'price_two', 'post_code')
    inlines = [
        PhotoInline,
    ]


admin.site.register(Flat, FlatAdmin)