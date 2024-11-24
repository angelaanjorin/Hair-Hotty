from django import forms


class ContactForm(forms.Form):
    name = forms.CharField(max_length=100, widget=forms.TextInput(attrs={
            'placeholder': 'Enter your name',
            'required': 'required'
            }))
    subject = forms.CharField(max_length=100, widget=forms.TextInput(attrs={
        'placeholder': 'Enter the subject',
        'required': 'required'
    }))
    email = forms.EmailField(widget=forms.EmailInput(attrs={
        'placeholder': 'Enter your email',
        'required': 'required'
    }))
    message = forms.CharField(widget=forms.Textarea(attrs={
        'rows': 5,
        'placeholder': 'Enter your message',
        'required': 'required'
    }))