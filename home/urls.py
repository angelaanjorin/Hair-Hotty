from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='home'),
    path('contact/', views.contact, name="contact"),
    path('about/', views.about, name="about"),
    path('privacy_policy/', views.privacy_policy, name="privacy_policy"),
    path('faq/', views.faq_page, name='faq_page'),
    path('returns/', views.returns, name='returns'),
    path('events/', views.events, name='events'),
]
