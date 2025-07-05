from django.urls import path

from catalog.apps import CatalogConfig

from . import views

app_name = CatalogConfig.name

urlpatterns = [
    path("home/", views.home, name="home"),
    path("contacts/", views.contacts, name="contacts"),
    path("product/<int:pk>/", views.product_detail, name="product_detail"),
    path("product/add/", views.product_add, name="product_add"),
    path('product/<int:pk>/edit/', views.product_edit, name='product_edit'),
]
