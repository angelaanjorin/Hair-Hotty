from django.contrib import admin
from .models import Review


# Register your models here.
class ReviewAdmin(admin.ModelAdmin):
    """
    Review Model Admin
    """

    list_display = (
        'product',
        'user',
        'review',
        'rating',
        'created_on',
    )

    list_editable = ('review',)
    readonly_fields = (
        'rating', 'user', 'product')


admin.site.register(Review, ReviewAdmin)
