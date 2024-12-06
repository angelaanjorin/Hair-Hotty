from django.contrib import admin
from django_summernote.admin import SummernoteModelAdmin
from .models import Product, PrimaryCategory, SpecialCategory


# Register your models here.

class ProductAdmin(SummernoteModelAdmin):
    list_display = (
        'name',
        'primary_category',
        'get_special_categories',
        'price',
        'rating',
        'image',
    )
    summernote_fields = ('description',)

    ordering = ('name',)

    def get_special_categories(self, obj):
        """
        Returns a comma-separated list of 
        special categories a product belongs to.
        """
        return ", ".join(
            [category.name for category in obj.special_categories.all()
        ])
    get_special_categories.short_description = 'Special Categories' 

    def save_model(self, request, obj, form, change):
        """
        Custom save_model method to ensure new products 
        don't have default special categories.
        """
        is_new = obj.pk is None  
        super().save_model(request, obj, form, change)
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