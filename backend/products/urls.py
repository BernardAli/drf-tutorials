from django.urls import path
from .views import ProductDetailAPIView, ProductListCreateAPIView, product_alt_view, \
    ProductUpdateAPIView, ProductDeleteAPIView


urlpatterns = [
    # path("", product_alt_view),
    path("", ProductListCreateAPIView.as_view()),
    path("<int:pk>", ProductDetailAPIView.as_view()),
    path("<int:pk>/update/", ProductUpdateAPIView.as_view()),
    path("<int:pk>/delete/", ProductDeleteAPIView.as_view()),
]