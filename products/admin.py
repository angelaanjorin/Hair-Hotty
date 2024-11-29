from django.contrib import admin
from .models import ProductSize, Product, Category

# Register your models here.
class ProductSizeInline(admin.TabularInline):
    model = ProductSize
    extra = 1  
    min_num = 0 


class ProductAdmin(admin.ModelAdmin):
    list_display = (
        'name',
        'category',
        'price',
        'rating',
        'image',
    )

    inlines = [ProductSizeInline]

    ordering = ('name',)

class CategoryAdmin(admin.ModelAdmin):  
    list_display = (
        'friendly_name',
        'name',
    )

# Register models in the admin site
admin.site.register(Product, ProductAdmin)
admin.site.register(Category, CategoryAdmin)