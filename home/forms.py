from django.forms import ModelForm
from logs.models import Data

class DataForm(ModelForm):
	class Meta:
		newEntry = Data
		fields = ['name', 'contact', 'manufacturer', 'model', 'price', 'description']
