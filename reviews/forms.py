from django import forms

from .models import Review


class ReviewForm(forms.ModelForm):
    """
    Form for Review Model - Add / Edit
    """

    class Meta:
        model = Review
        fields = ('review', 'rating',)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        
        # Set placeholder values
        placeholders = {
            'review': 'Your Review',
            'rating': '0',  # Assuming the rating is initially set to 0
        }
        
        for field, placeholder in placeholders.items():
            if field in self.fields:
                self.fields[field].widget.attrs.update({'placeholder': placeholder})

    def clean(self):
        cleaned_data = super().clean()
        review = cleaned_data.get('review')
        rating = cleaned_data.get('rating')

        # Ensure both the review and rating are provided
        if not review:
            raise forms.ValidationError('Review text is required.')

        if not rating:
            raise forms.ValidationError('Rating is required.')

        return cleaned_data
