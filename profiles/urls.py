from django.urls import path
from . import views

urlpatterns = [
    path('', views.profile, name='profile'),
    path('order_history/<order_number>', views.order_history, name='order_history'),
    path('profile/<int:profile_id>/orders/', views.my_orders, name='my_orders'),
    path('profile/<int:profile_id>/wishlist/', views.my_wishlist, name='my_wishlist'),
    path('profile/wishlist_add/<uuid:product_id>/',
        views.wishlist_add, name='wishlist_add'),
]