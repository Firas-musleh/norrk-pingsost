from django.contrib import admin
from django.db.models.fields.files import ImageFileDescriptor
from .models import *
from modeltranslation.admin import TranslationAdmin, TranslationTabularInline
# Register your models here.

admin.site.register(ProImag)

admin.site.register(ProductReview)
admin.site.register(PlatsReview)
admin.site.register(Home_images)
admin.site.register(Gallery)

class ProductImageInline(admin.TabularInline):
    model = ProImag
    extra = 6


class ProductAdmin(admin.ModelAdmin):

    list_display = ['name', 'slug', 'price',  'available', 'created',
                    'updated']
    list_filter = ['available', 'created', 'updated']
    list_editable = ['price',  'available']
    prepopulated_fields = {'slug': ('name',)}
    inlines = [ProductImageInline]

    class ProductAdmin(TranslationAdmin):
        model = Product


class PlatsSaluAdmin(admin.ModelAdmin):
    list_display = ['stan', 'adress',  'datom', 'start_time',
                    'end_time']


admin.site.register(PlatsSalu, PlatsSaluAdmin)

admin.site.register(Product, ProductAdmin)
