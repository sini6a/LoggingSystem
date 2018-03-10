from django.shortcuts import render
from django.http import HttpResponse

from django.template import loader
from .models import Data
from .forms import SearchForm
from django.middleware.csrf import get_token
from django.contrib.auth.decorators import login_required


# Create your views here.
# View for Logs Index
@login_required
def index(request):
    # data = Data.objects.order_by('-timestamp')
    # data = Data.objects.filter(data_owner_id=request.user).order_by('-timestamp')
    # template = loader.get_template('logs_index.html')

    # return HttpResponse(template.render({'data':data}, request))
    return render(request, 'logs_index.html')

# VIEW FOR SINGLE LOG
def log(request, log_id):
    data = Data.objects.get(pk=log_id)
    template = loader.get_template('single_log.html')

    context = {
        'data': data,
    }

    return HttpResponse(template.render(context, request))

# DELETE SINGLE LOG
def delete(request, log_id):
    Data.objects.filter(pk=log_id).delete()
    return render(request, 'deleted.html')


# SEARCH
def search(request):
    data = Data.objects.filter(data_owner_id=request.user).order_by('-timestamp')

    def countData(data):
        counter = data.count()
        return counter

    if request.method == "POST":
        search_text = request.POST['search_text']
    else:
        search_text = ''
        
    data = Data.objects.filter(data_owner_id=request.user, name__icontains=search_text).order_by('-timestamp')

    context = {
        'data': data,
        'counter': countData(data)
    }

    return render(request, 'ajax_search.html', context)
