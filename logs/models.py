from django.db import models

from django.core.validators import RegexValidator
from django.contrib.auth.models import User
from django.forms import ModelForm
from django.utils.translation import ugettext_lazy as _

# Create your models here.

class Data(models.Model):
        phone_regex = RegexValidator(regex=r'^\+?1?\d{9,15}$', message="Невалиден телефонски број. Пример: '+38970123123'")

        data_owner = models.ForeignKey(User, blank=True)
        timestamp = models.DateTimeField(auto_now=True)
        name = models.CharField(max_length=50)
        contact = models.CharField(validators=[phone_regex], max_length=17)
        manufacturer = models.CharField(max_length=25, blank=True)
        model = models.CharField(max_length=25, blank=True)
        price = models.IntegerField(blank=True, default=0)
        description = models.TextField(max_length=250, blank=True)

        def save(self, *args, **kwargs):
                super(Data, self).save(*args, **kwargs)

        def __str__(self):
            return self.name

class DataForm(ModelForm):
        class Meta:
                model = Data
                exclude = ['data_owner', 'timestamp']
                labels = {
                        'name': _("Регистарски таблици:"),
                        'contact': _("Контакт телефон:"),
                        'manufacturer': _("Производител:"),
                        'model': _("Модел:"),
                        'price': _("Цена:"),
                        'description': _("Опис:"),

                }
