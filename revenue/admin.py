from django.contrib import admin

from .models import RevenueCategory, RevenueSource, RevenueTransaction, TaxPayer


@admin.register(RevenueCategory)
class RevenueCategoryAdmin(admin.ModelAdmin):
    pass


@admin.register(RevenueSource)
class RevenueSourceAdmin(admin.ModelAdmin):
    list_display = ["name", "category"]
    list_filter = ["category"]
    search_fields = ["name"]


@admin.register(TaxPayer)
class TaxPayerAdmin(admin.ModelAdmin):
    list_display = ["name", "tin", "phone", "email"]
    search_fields = ["name", "tin"]


@admin.register(RevenueTransaction)
class RevenueTransactionAdmin(admin.ModelAdmin):
    list_display = ["tax_payer", "revenue_source", "amount"]
    date_hierarchy = "created"
    list_filter = ["revenue_source"]
    search_fields = ["tax_payer", "note"]
