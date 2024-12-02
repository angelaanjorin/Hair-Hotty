from django.contrib import admin
from .models import ProductSize, Product, PrimaryCategory, SpecialCategory

# Register your models here.
class ProductSizeInline(admin.TabularInline):
    model = ProductSize
    extra = 1  
    min_num = 0 


    def has_add_permission(self, request, obj=None):
        # Allow adding sizes only if the product has sizes
        return obj and obj.has_sizes



class ProductAdmin(admin.ModelAdmin):
    list_display = (
        'name',
        'primary_category',
        'get_special_categories',
        'price',
        'rating',
        'image',
    )
    
    def get_readonly_fields(self, request, obj=None):
        if obj and obj.sizes.exists():
            return ['stock_amount']
        return super().get_readonly_fields(request, obj)

    inlines = [ProductSizeInline]

    ordering = ('name',)

    def get_special_categories(self, obj):
        """
        Returns a comma-separated list of special categories a product belongs to.
        """
        return ", ".join([category.name for category in obj.special_categories.all()])
    get_special_categories.short_description = 'Special Categories' 

    def save_model(self, request, obj, form, change):
        """
        Custom save_model method to ensure new products don't have default special categories.
        """
        is_new = obj.pk is None  # Check if the product is new
        super().save_model(request, obj, form, change)  # Save the product
        if is_new:
            obj.special_categories.clear() 
            

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