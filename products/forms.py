from django import forms
from .widgets import CustomClearableFileInput
from .models import Product, PrimaryCategory, SpecialCategory


class ProductForm(forms.ModelForm):

    class Meta:
        model = Product
        fields = '__all__'

    image = forms.ImageField(label='Image', required=False, widget=CustomClearableFileInput)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        # Fetch primary categories and format them with friendly names
        primary_categories = PrimaryCategory.objects.all()
        primary_choices = [(c.id, c.get_friendly_name()) for c in primary_categories]
        self.fields['primary_category'].choices = primary_choices


        # Fetch special categories and format them with friendly names
        special_categories = SpecialCategory.objects.all()
        special_choices = [(c.id, c.get_friendly_name()) for c in special_categories]
        self.fields['special_categories'].choices = special_choices

        # Add consistent styling to all fields
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'border-black rounded-0'