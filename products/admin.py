from django.contrib import admin
from .models import ProductSize, Product, PrimaryCategory, SpecialCategory

# Register your models here.
class ProductSizeInline(admin.TabularInline):
    model = ProductSize
    extra = 1  
    min_num = 0 


class ProductAdmin(admin.ModelAdmin):
    list_display = (
        'name',
        'primary_category',
        'get_special_categories',
        'price',
        'rating',
        'image',
    )

    inlines = [ProductSizeInline]

    ordering = ('name',)

    def get_special_categories(self, obj):
        """
        Returns a comma-separated list of special categories a product belongs to.
        """
        return ", ".join([category.name for category in obj.special_categories.all()])
    get_special_categories.short_description = 'Special Categories' 


class PrimaryCategoryAdmin(admin.ModelAdmin):
    list_display = ('friendly_name', 'name')
    ordering = ('name',)


class SpecialCategoryAdmin(admin.ModelAdmin):
    list_display = ('friendly_name', 'name')
    ordering = ('name',)

# Register models in the admin site
admin.site.register(Product, ProductAdmin)
admin.site.register(PrimaryCategory, PrimaryCategoryAdmin)
admin.site.register(SpecialCategory, SpecialCategoryAdmin)