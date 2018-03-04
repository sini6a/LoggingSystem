from django.shortcuts import render
from django.http import HttpResponse

from django.template import loader
from .models import Data

# Create your views here.
def index(request):
	data = Data.objects.order_by('-timestamp')
	template = loader.get_template('logs/index.html')
	context = {
		'data':data,
	}
	return HttpResponse(template.render(context, request))

# VIEW FOR SINGLE LOG
def log(request, log_id):
	response = "You are at: %s <br>And looking at: "
	data = Data.objects.get(pk = log_id)
	template = loader.get_template('logs/log.html')
	context = {
		'data':data,
	}
	return HttpResponse(template.render(context, request))
