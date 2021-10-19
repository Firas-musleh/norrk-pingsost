from django.contrib import admin
from modeltranslation.admin import TranslationAdmin, TranslationTabularInline
# Register your models here.
from .models import Profile


admin.site.register(Profile)



