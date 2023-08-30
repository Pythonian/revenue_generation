from django.urls import path

from . import views

urlpatterns = [
    path("taxpayers/", views.tax_payer_list, name="tax_payer_list"),
    path("taxpayer/<int:id>/", views.tax_payer_detail, name="tax_payer_detail"),
    path("taxpayer/delete/", views.tax_payer_delete, name="tax_payer_delete"),
    path("transactions/", views.transaction_list, name="transaction_list"),
    path("transaction/delete/", views.transaction_delete, name="transaction_delete"),
    path("revenue-categories/", views.revenue_categories, name="revenue_categories"),
    path("revenue-sources/", views.revenue_sources, name="revenue_sources"),
    path("dashboard/", views.home, name="home"),
    path("", views.index, name="index"),
]
