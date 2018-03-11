from django.contrib import admin

from .models import (Category, Requirement, Provider, Support, Calification)


# Register your models here.
@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('code', 'name', 'description', 'active',)


@admin.register(Requirement)
class RequirementAdmin(admin.ModelAdmin):
    list_display = ('name', 'mandatory', 'active',)


@admin.register(Provider)
class ProviderAdmin(admin.ModelAdmin):
    list_display = ('code', 'name', 'active',)


@admin.register(Support)
class SupportAdmin(admin.ModelAdmin):
    list_display = ('provider', 'requirement', 'active',)


@admin.register(Calification)
class CalificationAdmin(admin.ModelAdmin):
    list_display = ('provider', 'value', 'user',)
