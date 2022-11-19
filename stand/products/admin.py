from django.contrib import admin

from .models import ExtraPhotos, Product, Tag, Works


class ExtraPhotosInLine(admin.StackedInline):
    model = ExtraPhotos


@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'slug')
    list_filter = ('name', 'slug')
    search_fields = ('name', 'slug')
    empty_value_display = '-пусто-'


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    inlines = [ExtraPhotosInLine, ]
    list_display = (
        'id', 'name', 'tag', 'price'
    )
    list_filter = ('name', 'tag')
    search_fields = ('name', 'tag')
    empty_value_display = '-пусто-'


@admin.register(Works)
class WorksAdmin(admin.ModelAdmin):
    list_display = (
        'id', 'tag', 'image'
    )
    list_filter = ('tag',)
    search_fields = ('id', 'tag')
    empty_value_display = '-пусто-'
