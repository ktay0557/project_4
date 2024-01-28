from django import forms
from .models import ContactRequest


class ContactForm(forms.ModelForm):
    """
    Form class for any user wanting to get in contact.
    """
    class Meta:
        """
        Specifies the Django model and the order of the fields.
        """
        model = ContactRequest
        fields = ('name', 'email', 'message')
