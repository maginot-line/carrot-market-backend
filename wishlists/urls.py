from django.urls import path
from .views import Wishlists, WishlistToggle

urlpatterns = [
    path("", Wishlists.as_view()),
    path("products/<int:product_pk>/", WishlistToggle.as_view()),
]
