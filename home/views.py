from django.shortcuts import render
from django.http import HttpResponse

from django.template import loader
from logs.models import DataForm
from django.contrib.auth import login, authenticate
from django.contrib.auth.decorators import login_required


# Create your views here.
@login_required
def index(request):
    template = loader.get_template('index.html')
    user = request.user
    if request.method == 'POST':
        form = DataForm(request.POST)
        if form.is_valid():
            data = form.save(commit=False)
            data.data_owner = request.user
            data = data.save()
            return render(request, 'submited.html')
    else:
        form = DataForm()
    context = {
	'form':form,
    }
    return HttpResponse(template.render(context, request))

