from django import forms

from .models import TaxPayer, RevenueCategory, RevenueTransaction, RevenueSource


class TaxPayerForm(forms.ModelForm):
    class Meta:
        model = TaxPayer
        fields = ["name", "address", "tin", "phone", "email"]


class RevenueTransactionForm(forms.ModelForm):
    class Meta:
        model = RevenueTransaction
        fields = ["tax_payer", "revenue_source", "amount", "note"]


class RevenueCategoryForm(forms.ModelForm):
    class Meta:
        model = RevenueCategory
        fields = ["name"]


class RevenueSourceForm(forms.ModelForm):
    class Meta:
        model = RevenueSource
        fields = ["name", "category", "description"]
