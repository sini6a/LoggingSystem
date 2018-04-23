from django import forms

from .models import Data
from django.utils.translation import ugettext_lazy as _


class DataForm(forms.ModelForm):
    class Meta:
        model = Data
        fields = ['name', 'contact', 'manufacturer', 'model', 'price', 'description']
        labels = {
            'name': _('Customer Name:'),
            'contact': _('Phone:'),
            'manufacturer': _('Manufacturer:'),
            'model': _('Model:'),
            'price': _('Price:'),
            'description': _('Description:'),

        }

class SearchForm(forms.Form):
    search_input = forms.CharField(max_length=30, required=False)

