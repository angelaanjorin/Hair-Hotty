"""
URL configuration for hair_hotty project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf import settings
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

from .views import handler403, handler404, handler500

urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include('allauth.urls')),
    path('djrichtextfield/', include('djrichtextfield.urls')),
    path('summernote/', include('django_summernote.urls')),
    path('', include('home.urls')),
    path('bag/', include('bag.urls')),
    path('blog/', include('blog.urls')),
    path('checkout/', include('checkout.urls')),
    path('products/', include('products.urls')),
    path('profile/', include('profiles.urls')),
    path('reviews/', include('reviews.urls')),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

handler403 = handler403
handler404 = handler404
handler500 = handler500