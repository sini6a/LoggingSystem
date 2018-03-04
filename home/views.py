from django.shortcuts import render
from django.http import HttpResponse

from django.template import loader
from logs.models import DataForm

# Create your views here.
def index(request):
	template = loader.get_template('home/index.html')	
	
	if request.method == 'POST':
		form = DataForm(request.POST)
		if form.is_valid():
			return HttpResponseRedirect('submited')
	else:
		form = DataForm()
	
	context = {
		'form':form
	}
	return HttpResponse(template.render(context, request))
