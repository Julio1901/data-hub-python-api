from django.contrib import admin

from .models import Investment


class Investments(admin.ModelAdmin):
    list_display = ('id', 'name', 'monetary_value', 'bank_name', 'type')
    list_display_links = ('id', 'name')
    search_fields = ('name',)


admin.site.register(Investment, Investments)
