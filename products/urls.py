from django.urls import path
from . import views


urlpatterns = [
    path("", views.ProductListView.as_view(), name="products"),
    path("create/", views.CreateProductView.as_view(), name="product_create"),
    path("<int:pk>/", views.ProductDetailView.as_view(), name="product_detail"),
]
