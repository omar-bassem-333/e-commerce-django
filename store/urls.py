from django.urls import path
from . import views


urlpatterns = [
    path("", views.home, name="home"),
    path("products/", views.product_list, name="product_list"),
    path("products/<int:id>/", views.product_detail, name="product_detail"),
    path("categories/<int:id>/", views.category_products, name="category_products"),
    path("products/create/", views.create_product, name="create_product"),
    path("products/<int:id>/update/", views.update_product, name="update_product"),
    path("products/<int:id>/delete/", views.delete_product, name="delete_product"),
]