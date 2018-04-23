from django.forms import ModelForm

from .models import Profile
from django.contrib.auth.models import User
from django.utils.translation import ugettext_lazy as _

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
