from django.urls import path
from . import views

urlpatterns = [
    path('', views.profile, name='profile'),
    path('order_history/<order_number>', views.order_history, name='order_history'),
    path('profile/wishlist_add/<uuid:product_id>/',
        views.wishlist_add, name='wishlist_add'),
]