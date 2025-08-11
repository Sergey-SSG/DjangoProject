from django.urls import path

from .views import (
    HomeView, ContactsView,
    ProductDetailView, ProductCreateView, ProductUpdateView, ProductDeleteView, ProductsByCategoryView
)

app_name = "catalog"

urlpatterns = [
    path("home/", HomeView.as_view(), name="home"),
    path("contacts/", ContactsView.as_view(), name="contacts"),
    path("product/<int:pk>/", ProductDetailView.as_view(), name="product_detail"),
    path("product/add/", ProductCreateView.as_view(), name="product_add"),
    path("product/<int:pk>/edit/", ProductUpdateView.as_view(), name="product_edit"),
    path('product/<int:pk>/delete/', ProductDeleteView.as_view(), name='product_delete'),
    path('category/<int:pk>/', ProductsByCategoryView.as_view(), name='products_by_category'),
]

# from django.urls import path
#
# from catalog.apps import CatalogConfig
#
# from . import views
#
# app_name = CatalogConfig.name
#
# urlpatterns = [
#     path("home/", views.home, name="home"),
#     path("contacts/", views.contacts, name="contacts"),
#     path("product/<int:pk>/", views.product_detail, name="product_detail"),
#     path("product/add/", views.product_add, name="product_add"),
#     path('product/<int:pk>/edit/', views.product_edit, name='product_edit'),
# ]
