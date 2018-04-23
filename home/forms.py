from django.forms import ModelForm
from logs.models import Data
from .models import Profile
from django.contrib.auth.models import User
from django.utils.translation import ugettext_lazy as _


class DataForm(ModelForm):
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

class UserForm(ModelForm):
    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'email')
        labels = {
            'first_name': _('First Name:'),
            'last_name': _('Last Name:'),
            'email': _('E-Mail:'),
        }

class ProfileForm(ModelForm):
    class Meta:
        model = Profile
        fields = ['language', 'company_name', 'company_logo', 'about_company']
        labels = {
            'language': _('Language:'),
            'company_name': _('Company Name:'),
            'company_logo': _('Logo:'),
            'about_company': _('Description:'),
        }
