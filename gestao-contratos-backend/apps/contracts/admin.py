from django.contrib import admin
from .models import Contract
from contractitems.models import ContractItem


class ContractItemInline(admin.TabularInline):
    model = ContractItem
    extra = 1


@admin.register(Contract)
class ContractAdmin(admin.ModelAdmin):
    list_display = ('id', 'number', 'title', 'client', 'employee', 'category', 'total_value', 'status')
    search_fields = ('number', 'title', 'description')
    list_filter = ('status', 'category')
    inlines = [ContractItemInline]