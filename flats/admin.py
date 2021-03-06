# -*- coding: utf-8 -*-

from django.contrib import admin

from import_export.admin import ImportExportModelAdmin

from .models import Flat, Photo


class PhotoInline(admin.TabularInline):
    model = Photo
    extra = 0

class FlatAdmin(ImportExportModelAdmin):
    list_display = ('available_from', 'property', 'post_code', 'room',
                    'area', 'price_one', 'price_two', 'bills',
                    'licensor', 'min_length')
    list_filter = ('area', 'licensor', 'property', 'price_one', 'price_two',
                   'available_from', 'n_b')
    search_fields = ('licensor', 'available_from', 'property', 'area', 'n_b',
                     'price_one', 'price_two', 'post_code')
    inlines = [
        PhotoInline,
    ]


admin.site.register(Flat, FlatAdmin)