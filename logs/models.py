from django.db import models

from django.contrib.auth.models import User
from django.utils.translation import ugettext_lazy as _

# Create your models here.

class Data(models.Model):
        data_owner = models.ForeignKey(User, blank=True)
        timestamp = models.DateTimeField(auto_now=True)
        name = models.CharField(max_length=50)
        contact = models.CharField(max_length=17)
        manufacturer = models.CharField(max_length=25, blank=True)
        model = models.CharField(max_length=25, blank=True)
        price = models.IntegerField(blank=True, default=0)
        description = models.TextField(max_length=250, blank=True)

        def save(self, *args, **kwargs):
                super(Data, self).save(*args, **kwargs)

        def __str__(self):
            return self.name
