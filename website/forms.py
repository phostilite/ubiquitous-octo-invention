# forms.py
from django import forms
from .models import NewsletterSubscription

class NewsletterSubscriptionForm(forms.ModelForm):
    class Meta:
        model = NewsletterSubscription
        fields = ['email']
        widgets = {
            'email': forms.EmailInput(attrs={'class': 'flex-grow px-3 py-2 bg-gray-800 text-white rounded-l-md focus:outline-none mb-2 sm:mb-0', 'placeholder': 'Your email'}),
        }
