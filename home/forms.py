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
            'name': _('Регистарски таблици:'),
            'contact': _('Контакт телефон:'),
            'manufacturer': _('Производител:'),
            'model': _('Модел:'),
            'price': _('Цена:'),
            'description': _('Опис:'),

        }

class UserForm(ModelForm):
    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'email')
        labels = {
            'first_name': _('Име:'),
            'last_name': _('Презиме:'),
            'email': _('E-Mail:'),
        }

class ProfileForm(ModelForm):
    class Meta:
        model = Profile
        fields = ['company_name', 'company_logo', 'about_company']
        labels = {
            'company_name': _('Име на компанијата:'),
            'company_logo': _('Лого на компанијата:'),
            'about_company': _('Опис на компанијата:'),
        }
