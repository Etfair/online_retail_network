from django.contrib import admin
from main.models import Network, Product


@admin.register(Network)
class NetworkAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'country', 'city', 'street', 'house_number',)
    list_filter = ('country',)


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'model', 'release_date', 'supplier_link', 'supplier', 'debt_to_supplier', 'creation_time')
    actions = ['clear_debt_to_supplier']

    def supplier_link(self, obj):
        return f'<a href="/admin/main/network/{obj.supplier.id}/" a>'
    supplier_link.allow_tags = True
    supplier_link.short_description = 'Ссылка на поставщика'

    def clear_debt_to_supplier(self, request, queryset):
        queryset.update(debt_to_supplier=0)
    clear_debt_to_supplier.short_description = "Очистить задолженность перед поставщиком"
